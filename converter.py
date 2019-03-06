import os
import importlib
from flask import Flask, jsonify, abort, request
import pdfkit

class Convert:
    def __init__(self):
        self.api()

    def api(self):
        app = Flask(__name__)

        @app.route('/api/converter', methods=['GET'])
        def convert():
            url = request.args.get('url')
            filename = request.args.get('filename')
            outfile = pdfkit.from_url(url, filename)
            return jsonify({"url":url, 'filename': filename})

        app.run(debug=False)

classobject = Convert()
