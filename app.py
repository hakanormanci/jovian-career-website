from flask import Flask, render_template, jsonify

app=Flask(__name__)

JOBS=[
  {"Id":1, "Title":"Data Analyst", "Location":"Bengaluru, India", "Salary":"Rs. 10,00,000"},
  {"Id":2, "Title":"Data Scientist", "Location":"Delhi, India", "Salary" :"Rs. 15,00,000"},
  {"Id":3, "Title":"Frontend Engineer", "Location":"Remote"},
  {"Id":4, "Title":"Backend Engineer", "Location":"San Francisco, USA", "Salary": "$120,000"}
]

@app.route("/")
def hello_world():
  return render_template('home.html', joblar=JOBS,
                        company_name="Jovian")

@app.route("/api/jobs")
def list_jobs():
  return(jsonify(JOBS))

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)