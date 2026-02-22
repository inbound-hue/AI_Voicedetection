from flask import Flask, render_template, request, redirect, url_for
from threading import Thread
import os

# Import functions from email_reciever.py
from email_reciever import process_emails

# Flask app setup
app = Flask(__name__)   # Flask automatically looks for "templates" folder


@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        target_email = request.form["email"].strip().lower()

        print(f"Received email: {target_email}")

        # Run email processing in background
        start_email_processing(target_email)

        return redirect(url_for("success"))

    return render_template("index.html")


@app.route("/success")
def success():
    return "Email processing started successfully!"


def start_email_processing(target_email):
    print(f"Starting background processing for: {target_email}")
    thread = Thread(target=process_emails, args=(target_email,))
    thread.daemon = True
    thread.start()


if __name__ == "__main__":
    # Cloud Run uses PORT environment variable
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)




