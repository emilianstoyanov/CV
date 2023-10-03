from flask import Flask, render_template, request, redirect, url_for
import smtplib
from email.message import EmailMessage

app = Flask(__name__)

# Replace these placeholders with your actual email server details
SMTP_SERVER = 'smtp-mail.outlook.com'
SMTP_PORT = 587
EMAIL_USERNAME = 'emilian.stoyanov@outlook.com'
EMAIL_PASSWORD = 'ppj9UkdMhYzpwKLkfU4x'

@app.route('/', methods=['GET', 'POST'])
def contact_form():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']

        msg = EmailMessage()
        msg.set_content(f"From: {name}\nEmail: {email}\n\n{message}")
        msg['Subject'] = 'Contact Form Submission'
        msg['From'] = EMAIL_USERNAME
        msg['To'] = 'emilian.stoyanov@outlook.com'  # Replace with the recipient's email address

        try:
            with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
                server.starttls()
                server.login(EMAIL_USERNAME, EMAIL_PASSWORD)
                server.send_message(msg)
            return redirect(url_for('success'))
        except Exception as e:
            return str(e)

    return render_template('index.html')  # Create an HTML template for your contact form

@app.route('/success')
def success():
    return "Message sent successfully!"

# if __name__ == '__main__':
#     app.run(debug=True)
    

if __name__ == "__main__":
    from waitress import serve
    serve(app, host="0.0.0.0", port=8080)
