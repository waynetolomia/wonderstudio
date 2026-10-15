#!/usr/bin/env python3
"""Local preview launcher. Python 3.10+. No third-party Python dependencies."""
import argparse
import functools
import http.server
from pathlib import Path
import threading
import webbrowser

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--port',type=int,default=8000)
    args=parser.parse_args()
    if not 1024<=args.port<=65535:
        parser.error('Choose a port from 1024 to 65535.')
    directory=Path(__file__).resolve().parent
    handler=functools.partial(http.server.SimpleHTTPRequestHandler,directory=str(directory))
    try:
        server=http.server.ThreadingHTTPServer(('127.0.0.1',args.port),handler)
    except OSError as exc:
        parser.exit(1,f'Could not start the local server: {exc}\nTry: python serve.py --port 8010\n')
    address=f'http://localhost:{args.port}/'
    print(f'Wonder Global Studio: {address}\nKeep this window open. Press Ctrl+C to stop.')
    threading.Timer(0.5,lambda:webbrowser.open(address)).start()
    try:server.serve_forever()
    except KeyboardInterrupt:print('\nServer stopped.')
    finally:server.server_close()
if __name__=='__main__':main()
