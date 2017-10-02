from flask import *
import mlab
from mongoengine import *

mlab.connect()

class GirlType(Document):
    name = StringField()
    image = StringField()
    description = StringField()

girl_type = GirlType(name="Gái tiểu thư", image="https://via.placeholder.com/400x200", description="Gọn gàng sạch sẽ, thích con trai chơi thể thao giỏi, nghệ thuật giỏi và đặc biệt hơn thích đến những nơi sang chảnh")
girl_type.save()
#1.Connect to mlab
#2.Add some data
#3.Get data for render_template


app = Flask(__name__)

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


@app.route("/about")
def about():
    return render_template("about.html")


if __name__ == '__main__':
  app.run(debug=True)
