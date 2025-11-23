from flask import Flask

# Pass the current module's name to Flask so it can locate resources
# and set the application's root path correctly.
app = Flask(__name__)


@app.route("/")
def home():
  return """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Home Page</title>
  <style>
    body {
      font-family: Arial, sans-serif;
      margin: 0;
      padding: 0;
      background-color: #f4f4f4;
    }
    header {
      background-color: #333;
      color: #fff;
      padding: 20px;
      text-align: center;
    }
    nav {
      background: #444;
      padding: 10px;
      text-align: center;
    }
    nav a {
      color: white;
      margin: 0 15px;
      text-decoration: none;
      font-weight: bold;
    }
    nav a:hover {
      text-decoration: underline;
    }
    .container {
      padding: 40px;
      text-align: center;
    }
    .btn {
      background: #333;
      color: white;
      padding: 10px 20px;
      text-decoration: none;
      border-radius: 5px;
    }
    .btn:hover {
      background: #555;
    }
  </style>
</head>
<body>
  <header>
    <h1>Welcome to My Website</h1>
  </header>

  <nav>
    <a href="#">Home</a>
    <a href="/about">About Me</a>
  </nav>

  <div class="container">
    <h2>Hello!</h2>
    <p>This is my simple home page connected to the About Me page.</p>
    <a class="btn" href="/about">Go to About Me</a>
  </div>
</body>
</html>"""

@app.route("/about")
def about():
  return """<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>About Me — Your Name</title>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700&display=swap" rel="stylesheet">
  <style>
    :root{
      --bg:#0f1724;
      --card:#0b1220;
      --muted:#94a3b8;
      --accent:#06b6d4;
      --glass: rgba(255,255,255,0.03);
      --radius:12px;
      color-scheme: dark;
    }
    *{box-sizing:border-box}
    body{font-family:Inter,system-ui,-apple-system,"Segoe UI",Roboto,"Helvetica Neue",Arial; margin:0; background:linear-gradient(180deg,#071025 0%, #071a2a 100%); color:#e6eef6; padding:32px}
    .container{max-width:1000px; margin:0 auto;}

    header{display:flex;gap:20px;align-items:center;margin-bottom:28px}
    .avatar{width:120px;height:120px;border-radius:18px;overflow:hidden;flex:0 0 120px;background:var(--glass);display:flex;align-items:center;justify-content:center;border:1px solid rgba(255,255,255,0.04)}
    .avatar img{width:100%;height:100%;object-fit:cover}
    .intro{flex:1}
    .name{font-size:1.6rem;font-weight:700;margin:0}
    .role{color:var(--muted);margin-top:6px}

    .grid{display:grid;grid-template-columns:1fr 320px;gap:20px}

    .card{background:linear-gradient(180deg, rgba(255,255,255,0.02), rgba(255,255,255,0.01));padding:18px;border-radius:var(--radius);box-shadow:0 6px 20px rgba(2,6,23,0.6);border:1px solid rgba(255,255,255,0.03)}

    h2{margin:0 0 12px 0;font-size:1.05rem}
    p{color:var(--muted);line-height:1.6}

    .skills{display:flex;flex-wrap:wrap;gap:8px}
    .chip{background:rgba(255,255,255,0.03);padding:6px 10px;border-radius:999px;font-size:0.9rem;border:1px solid rgba(255,255,255,0.02)}

    .meta{display:flex;flex-direction:column;gap:10px}
    .meta .row{display:flex;justify-content:space-between;color:var(--muted)}

    .contact a{color:var(--accent);text-decoration:none}

    footer{margin-top:28px;text-align:center;color:var(--muted);font-size:0.9rem}

    /* responsive */
    @media (max-width:880px){
      .grid{grid-template-columns:1fr;}
      header{flex-direction:row}
      .avatar{width:96px;height:96px}
    }

    /* small utilities */
    .btn{display:inline-block;padding:8px 12px;border-radius:10px;background:linear-gradient(90deg,var(--accent),#0ea5a4);color:#021014;text-decoration:none;font-weight:600}
    .section{margin-bottom:18px}
    .timeline{display:flex;flex-direction:column;gap:12px}
    .timeline-item{padding:12px;border-radius:10px;background:rgba(255,255,255,0.01);border:1px solid rgba(255,255,255,0.02)}
  </style>
</head>
<body>
  <div class="container">
    <header>
      <div class="avatar card">
        <!-- Replace the src with your image path or URL -->
        <img src="https://via.placeholder.com/300x300.png?text=Your+Photo" alt="Your Name">
      </div>
      <div class="intro">
        <h1 class="name">Your Name</h1>
        <div class="role">Student · Developer · Learner</div>
        <p style="margin-top:10px;color:var(--muted)">A short one-line bio. Example: "I build small Python tools, learn web development, and love solving problems."</p>
        <div style="margin-top:12px;display:flex;gap:10px;align-items:center">
          <a class="btn" href="#contact">Contact Me</a>
          <a class="btn" href="#resume" style="background:transparent;border:1px solid rgba(255,255,255,0.06);color:var(--accent)">Download Resume</a>
        </div>
      </div>
    </header>

    <main class="grid">
      <!-- Left column -->
      <div>
        <section class="card section">
          <h2>About Me</h2>
          <p>Write 2–3 sentences about yourself. Mention your interests, what you study or work on, and what you're learning right now. For example: "I am a beginner web developer learning HTML, CSS and JavaScript. I also enjoy Python programming and building small projects to practise."</p>
        </section>

        <section class="card section">
          <h2>Skills</h2>
          <div class="skills">
            <span class="chip">Python</span>
            <span class="chip">HTML</span>
            <span class="chip">CSS</span>
            <span class="chip">JavaScript</span>
            <span class="chip">Git</span>
            <span class="chip">Data Structures</span>
          </div>
        </section>

        <section class="card section">
          <h2>Education</h2>
          <div class="timeline">
            <div class="timeline-item">
              <strong>Degree or Course</strong>
              <div class="row" style="margin-top:6px;color:var(--muted)">Institution · <span>Year</span></div>
              <p style="margin-top:8px;color:var(--muted)">Short details: major subjects, achievements, CGPA, or projects.</p>
            </div>

            <div class="timeline-item">
              <strong>Another Course / Certification</strong>
              <div class="row" style="margin-top:6px;color:var(--muted)">Platform · <span>Year</span></div>
              <p style="margin-top:8px;color:var(--muted)">Short details about the certification.</p>
            </div>
          </div>
        </section>

        <section class="card section">
          <h2>Projects</h2>
          <div class="timeline">
            <div class="timeline-item">
              <strong>Project Title</strong>
              <div class="row" style="margin-top:6px;color:var(--muted)">Tools: Python, Flask · <span>2025</span></div>
              <p style="margin-top:8px;color:var(--muted)">One-line description and a link: <a href="#" style="color:var(--accent)">View on GitHub</a></p>
            </div>
          </div>
        </section>
      </div>

      <!-- Right column -->
      <aside>
        <div class="card section meta">
          <h2>Contact</h2>
          <div class="row"><span>Email</span><a href="mailto:you@example.com">you@example.com</a></div>
          <div class="row"><span>Phone</span><a href="tel:+911234567890">+91 12345 67890</a></div>
          <div class="row"><span>Location</span><span style="color:var(--muted)">Your City, Country</span></div>
        </div>

        <div class="card section">
          <h2>Quick Facts</h2>
          <p class="muted">Available for internships · Open to collaborations · Fast learner</p>
          <div style="margin-top:10px" class="skills">
            <span class="chip">Open to work</span>
            <span class="chip">Internship</span>
            <span class="chip">Remote</span>
          </div>
        </div>

        <div class="card section">
          <h2>Social</h2>
          <p style="color:var(--muted);margin:0 0 8px 0">Connect on</p>
          <div style="display:flex;flex-direction:column;gap:8px">
            <a href="#" style="color:var(--accent);text-decoration:none">GitHub</a>
            <a href="#" style="color:var(--accent);text-decoration:none">LinkedIn</a>
            <a href="#" style="color:var(--accent);text-decoration:none">Twitter / X</a>
          </div>
        </div>

        <div id="resume" class="card section">
          <h2>Resume</h2>
          <p style="color:var(--muted)">Replace the file link below with your resume (PDF).</p>
          <a href="#" class="btn">Download Resume</a>
        </div>

        <div id="contact" class="card section">
          <h2>Send a Message</h2>
          <form onsubmit="sendMessage(event)">
            <div style="display:flex;flex-direction:column;gap:8px">
              <input id="name" type="text" placeholder="Your name" required style="padding:10px;border-radius:8px;border:1px solid rgba(255,255,255,0.04);background:transparent;color:inherit">
              <input id="email" type="email" placeholder="Your email" required style="padding:10px;border-radius:8px;border:1px solid rgba(255,255,255,0.04);background:transparent;color:inherit">
              <textarea id="message" rows="4" placeholder="Message" required style="padding:10px;border-radius:8px;border:1px solid rgba(255,255,255,0.04);background:transparent;color:inherit"></textarea>
              <button class="btn" type="submit">Send</button>
            </div>
          </form>
          <p id="sent" style="color:var(--muted);margin-top:8px;display:none">Message simulated (this is demo only).</p>
        </div>
      </aside>
    </main>

    <footer>
      Built with ❤️ — Replace content with your details.
    </footer>
  </div>

  <script>
    function sendMessage(e){
      e.preventDefault();
      // This is only a demo. In a real site you'd POST to your server or use an email service.
      document.getElementById('sent').style.display = 'block';
      setTimeout(()=>{document.getElementById('sent').style.display='none'},4000);
    }
  </script>
</body>
</html>"""

if __name__ == '__main__':
  # Run the app when this file is executed directly
  app.run(debug=True)