from flask import *
import search
import unittest
import shutil

app = Flask(__name__)

class Test(unittest.TestCase):
    def test_search_1(self):
        shutil.copyfile('testing/test-1.txt', 'testing.txt')
        self.assertEqual(search.Search('testing.txt'), 'тест')

    def test_search_2(self):
        shutil.copyfile('testing/test-2.txt', 'testing.txt')
        self.assertEqual(search.Search('testing.txt'), 'котёнок')


@app.route('/')
def main():
    return render_template("run.html")

@app.route('/success', methods=['POST'])
def success():
    try:
        if request.method == 'POST':
            word = ''
            f = request.files['file']
            f.save(f.filename)
            print(f.filename)
            word = search.Search(f.filename)
            return render_template("success.html", word=word)
    except:
        return render_template("run.html")

@app.route("/success", methods=["POST"])
def move_forward():
    return render_template("run.html")

if __name__ == '__main__':
    unittest.main()
    app.run(debug=True)