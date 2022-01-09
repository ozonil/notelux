Note taking app in flask.

TODO:
* Allow users to delete information.
* Add more formats of data.

Getting started:
1. Clone the repo:
```
git clone https://github.com/ozonil/notelux
```
2. Create a virtual environment within in the directory and activate it:
```
python3 -m venv venv
source venv/bin/activate
```
3. Install the requirements:
```
pip install -r requirements.txt
```
4. Applying changes in migrations and creating the database:
```
flask db upgrade
```
5. Run the app:
```
flask run
```