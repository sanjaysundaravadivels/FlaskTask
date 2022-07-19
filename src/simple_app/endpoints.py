from flask import request,render_template
def api_routes(endpoints):
    @endpoints.route('/register', methods=['GET'])
    def login():
        return render_template("index.html")

    return endpoints