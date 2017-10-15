from flask import *
import os
import mlab
from models.girl_type import GirlType, dump_data

mlab.connect()

dump_data()

girl_type = GirlType(name="Gái tiểu thư", image="https://via.placeholder.com/400x200", description="Gọn gàng sạch sẽ, thích con trai chơi thể thao giỏi, nghệ thuật giỏi và đặc biệt hơn thích đến những nơi sang chảnh")
girl_type.save()
#1.Connect to mlab
#2.Add some data
#3.Get data for render_template


app = Flask(__name__)
app.config["SECRET_KEY"] = "QJNAS0as09dqw99)=,zvckj"

gt = [
    {
        "name": "Gái tiểu thư",
        "image": "https://via.placeholder.com/400x200",
        "description": "Gọn gàng sạch sẽ, thích con trai chơi thể thao giỏi, nghệ thuật giỏi và đặc biệt hơn thích đến những nơi sang chảnh"
    },
    {
        "name": "Gái ngoan",
        "image": "https://via.placeholder.com/400x200",
        "description": "Tính khá bình dân, ăn mặc gọn gàng, chăm học, cẩn thận, hay xuất hiện ở thư viện"
    },
    {
        "name": "Gái hư",
        "image": "https://via.placeholder.com/400x200",
        "description": "Xem ảnh sẽ biết!"
    }
]

@app.route('/')
def index():
    return render_template("index.html", girl_types=GirlType.objects())

@app.route("/girl_type/<girl_id>")
def girl_type_detail(girl_id):
    girl_type = GirlType.objects().with_id(girl_id)
    if girl_type is not None:
        return render_template("girl_type_detail.html", girl_type=girl_type)
    else:
        return "<h4>Không tìm thấy loại gái này</h4>"

@app.route("/edit_girl_type/<girl_id>", methods=["GET", "POST"])
def edit_girl_type(girl_id):
    girl_type = GirlType.objects().with_id(girl_id)
    if request.method == "GET":
        if girl_type is not None:
            return render_template("edit.html", girl_type=girl_type)
        return "Tuyệt chủng rồi"
    elif request.method == "POST":
        form = request.form

        name = form["name"]
        image = form["image"]
        description = form["description"]

        girl_type.update(set__name=name, set__image=image, set__description=description)
        return "Successfully Updated"

@app.route('/admin')
def admin():
    if "admin" not in session:
        return abort(401)
    else:
        return render_template("admin.html", girl_types=GirlType.objects())

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    elif request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if username=="admin" and password=="admin":
            session["admin"] = True
            return redirect("/admin")
        else:
            return abort(401)

@app.route("/images/<image_name>")
def image(image_name):
    image_folder = os.path.join(app.root_path, 'static', 'images')
    return send_from_directory(image_folder, image_name)

@app.route("/delete_girl_type/<girl_id>")
def delete_girl_type(girl_id):
    girl_type = GirlType.objects().with_id(girl_id)
    if girl_type is not None:
        girl_type.delete()
    return redirect("/admin")

@app.route("/about")
def about():
    return render_template("about.html")

if __name__ == '__main__':
  app.run(debug=True)
