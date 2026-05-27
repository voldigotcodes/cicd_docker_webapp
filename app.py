from datetime import datetime, timezone
from flask import Flask, jsonify, render_template_string, request
import os

app = Flask(__name__)

@app.route('/')
def home():
    return render_template_string('''
    <!doctype html>
        <html lang="en">
        <head>
          <meta charset="UTF-8" />
          <meta name="viewport" content="width=device-width, initial-scale=1.0" />
          <title>Welcome to the CICD Docker Web App</title>
          <script src="https://cdn.tailwindcss.com"></script>
        </head>
        <body class="min-h-screen bg-slate-950 flex items-center justify-center">
          <main class="px-6 text-center">
            <h1 class="text-6xl md:text-8xl font-extrabold tracking-tight bg-gradient-to-r from-cyan-300 via-teal-300 to-blue-900 bg-clip-text text-transparent">
              Welcome to the CICD Docker Web App!
            </h1>
            <p class="mt-6 text-lg text-slate-300 tracking-tight bg-gradient-to-r from-cyan-300 via-teal-300 to-blue-900 bg-clip-text text-transparent">
              This is a simple Flask application designed to demonstrate CI/CD practices with Docker.
            </p>
          </main>
        </body>
        </html>
    ''')

@app.route('/health')
def health():
    payload = {
        'status': 'healthy',
        'service': 'CICD Docker Web App',
        'message': 'The application is running smoothly.',
        'timestamp': datetime.now(timezone.utc).isoformat()
    }
    accept_header = request.headers.get("Accept", "")
    wants_html = "text/html" in accept_header and request.args.get("format") != "json"

    if not wants_html:
        return jsonify(payload)

    return render_template_string(
        """
        <!doctype html>
        <html lang="en">
        <head>
          <meta charset="UTF-8" />
          <meta name="viewport" content="width=device-width, initial-scale=1.0" />
          <title>Health Check</title>
          <script src="https://cdn.tailwindcss.com"></script>
        </head>
        <body class="min-h-screen bg-gradient-to-br from-slate-950 via-blue-950 to-slate-900 text-slate-100 flex items-center justify-center p-6">
          <main class="w-full max-w-2xl rounded-3xl border border-cyan-400/20 bg-slate-900/70 backdrop-blur-xl shadow-2xl shadow-cyan-900/30 p-8 md:p-10">
            <div class="flex items-center justify-between gap-4">
              <h1 class="text-4xl md:text-5xl font-black tracking-tight bg-gradient-to-r from-cyan-300 via-teal-300 to-blue-400 bg-clip-text text-transparent">
                System Healthy
              </h1>
              <span class="inline-flex items-center gap-2 rounded-full bg-emerald-500/20 px-3 py-1 text-sm font-semibold text-emerald-300 border border-emerald-400/30">
                <span class="h-2.5 w-2.5 rounded-full bg-emerald-300 animate-pulse"></span>
                OK
              </span>
            </div>
            <p class="mt-4 text-slate-300">
              Service is up and responding normally.
            </p>
            <div class="mt-8 grid gap-4 md:grid-cols-2">
              <div class="rounded-2xl bg-slate-800/70 border border-slate-700 p-4">
                <p class="text-xs uppercase tracking-wide text-slate-400">Service</p>
                <p class="mt-1 text-lg font-semibold text-cyan-200">{{ service }}</p>
              </div>
              <div class="rounded-2xl bg-slate-800/70 border border-slate-700 p-4">
                <p class="text-xs uppercase tracking-wide text-slate-400">Timestamp (UTC)</p>
                <p class="mt-1 text-sm md:text-base font-medium text-slate-200 break-all">{{ timestamp }}</p>
              </div>
            </div>
          </main>
        </body>
        </html>
        """,
        service=payload["service"],
        timestamp=payload["timestamp"],
    )

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 8002))
    app.run(host='0.0.0.0', port=port)