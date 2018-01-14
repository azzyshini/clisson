#!/usr/bin/env python

import argparse
import importlib

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Clisson web manager app.')
    parser.add_argument('-r','--ignore-reloader', default=True, action='store_false', 
                        help='(Werkzeug) Use Flask auto reloader.', required=False)
    parser.add_argument('-w','--processes', default=1, type=int,
                        help='(Werkzeug) If greater than 1 then handle '
                        'each request in a new process up to this maximum '
                        'number of concurrent processes.', required=False)
    parser.add_argument('-p','--port', default=5000, type=int,
                        help='(Werkzeug) Port number.', required=False)
    parser.add_argument('-t','--threaded', default=False, action='store_true',
                        help='(Werkzeug) Should the process handle each '
                        'request in a separate thread?', required=False)
    parser.add_argument('-a','--app', type=str, choices=["clisson"],
                        help='Application name. Currently supported '
                        'app is clisson', required=True)

    args = parser.parse_args()

    app = getattr(importlib.import_module(args.app), 'app')
    app.run(host = '0.0.0.0', port=args.port,
            debug=False, use_reloader=args.ignore_reloader,
            processes=args.processes, threaded=args.threaded)
