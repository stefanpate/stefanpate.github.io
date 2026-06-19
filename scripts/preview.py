#!/usr/bin/env python3
"""Range-capable static file server for previewing the built _site/.

Jekyll's default WEBrick server mishandles HTTP Range requests, which causes
video (mp4) playback to stall or reset (Errno::ECONNRESET) in Chrome. This
server implements 206 Partial Content properly, so video plays smoothly.

Usage:
    bundle exec jekyll build      # generate _site/
    python3 scripts/preview.py    # serve _site/ at http://localhost:4001
"""
import http.server
import os
import re
import sys

ROOT = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "_site")
PORT = 4001


class RangeHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=ROOT, **kwargs)

    def send_head(self):
        # Drop query strings (e.g. ?v=2 cache-busters) before resolving the file.
        self.path = self.path.split("?", 1)[0]
        path = self.translate_path(self.path)
        if os.path.isdir(path):
            return super().send_head()
        try:
            f = open(path, "rb")
        except OSError:
            self.send_error(404, "File not found")
            return None

        fs = os.fstat(f.fileno())
        size = fs.st_size
        ctype = self.guess_type(path)
        rng = self.headers.get("Range")

        if rng is None:
            self.send_response(200)
            self.send_header("Content-Type", ctype)
            self.send_header("Content-Length", str(size))
            self.send_header("Accept-Ranges", "bytes")
            self.end_headers()
            return f

        m = re.match(r"bytes=(\d*)-(\d*)", rng)
        if not m:
            self.send_error(416, "Invalid Range")
            f.close()
            return None
        start = int(m.group(1)) if m.group(1) else 0
        end = int(m.group(2)) if m.group(2) else size - 1
        end = min(end, size - 1)
        if start > end:
            self.send_error(416, "Range Not Satisfiable")
            f.close()
            return None

        self.send_response(206)
        self.send_header("Content-Type", ctype)
        self.send_header("Content-Range", f"bytes {start}-{end}/{size}")
        self.send_header("Content-Length", str(end - start + 1))
        self.send_header("Accept-Ranges", "bytes")
        self.end_headers()
        f.seek(start)
        self._range = (start, end)
        return f

    def copyfile(self, source, outputfile):
        rng = getattr(self, "_range", None)
        if rng is None:
            return super().copyfile(source, outputfile)
        start, end = rng
        remaining = end - start + 1
        while remaining > 0:
            chunk = source.read(min(64 * 1024, remaining))
            if not chunk:
                break
            try:
                outputfile.write(chunk)
            except (BrokenPipeError, ConnectionResetError):
                break  # browser closed the connection mid-seek; normal for video
            remaining -= len(chunk)


def main():
    if not os.path.isdir(ROOT):
        sys.exit(f"{ROOT} does not exist — run 'bundle exec jekyll build' first.")
    http.server.ThreadingHTTPServer.daemon_threads = True
    with http.server.ThreadingHTTPServer(("127.0.0.1", PORT), RangeHandler) as httpd:
        print(f"Serving {ROOT} at http://localhost:{PORT}  (Ctrl-C to stop)")
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            pass


if __name__ == "__main__":
    main()
