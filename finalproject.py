from flask import Flask, render_template, request, redirect, jsonify, url_for
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup_weapons import Categories, CategoryItem, Base

app = Flask(__name__)

engine = create_engine('sqlite:///weaponsGuide.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()


@app.route('/weaponsGuide/<int:category_id>/menu/JSON')
def weaponsGuideJSON(category_id):
    DBSession = sessionmaker(bind=engine)
    session = DBSession()
    categories = session.query(Categories).filter_by(id=category_id).one()
    items = session.query(CategoryItem).filter_by(
        category_id=category_id).all()
    return jsonify(items=[i.serialize for i in items])


@app.route('/weaponsGuide/<int:category_id>/weapon/<int:items_id>/JSON')
def itemJSON(category_id, items_id):
    DBSession = sessionmaker(bind=engine)
    session = DBSession()
    Weapon = session.query(CategoryItem).filter_by(id=items_id).one()
    return jsonify(Weapon=Weapon.serialize)


@app.route('/weaponsGuide/JSON')
def categoryJSON():
    DBSession = sessionmaker(bind=engine)
    session = DBSession()
    categories = session.query(Categories).all()
    return jsonify(categories=[r.serialize for r in categories])


# Show all categories
@app.route('/')
@app.route('/weaponsGuide/')
def showCategories():
    DBSession = sessionmaker(bind=engine)
    session = DBSession()
    categories = session.query(Categories).all()
    # return "This page will show all my restaurants"
    return render_template('home.html', categories = categories)


# Create a new category
@app.route('/weaponsGuide/new/', methods=['GET', 'POST'])
def newCategory():
    DBSession = sessionmaker(bind=engine)
    session = DBSession()
    if request.method == 'POST':
        newWeapon = Categories(name=request.form['name'])
        session.add(newWeapon)
        session.commit()
        return redirect(url_for('showCategories'))
    else:
        return render_template('newCategory.html')

# Edit a category
@app.route('/weaponsGuide/<int:category_id>/edit/', methods=['GET', 'POST'])
def editCategory(category_id):
    DBSession = sessionmaker(bind=engine)
    session = DBSession()
    editedCategory = session.query(
        Categories).filter_by(id=category_id).one()
    if request.method == 'POST':
        if request.form['name']:
            editedCategory.name = request.form['name']
            session.commit()
            return redirect(url_for('showCat', category_id = category_id ))
    else:
        return render_template(
            'editCategory.html', category=editedCategory)


# Delete a category
@app.route('/weaponsGuide/<int:category_id>/delete/', methods=['GET', 'POST'])
def deleteCategory(category_id):
    DBSession = sessionmaker(bind=engine)
    session = DBSession()
    categoryToDelete = session.query(
        Categories).filter_by(id=category_id).one()
    if request.method == 'POST':
        session.delete(categoryToDelete)
        session.commit()
        return redirect(
            url_for('showCategories'))
    else:
        return render_template(
            'deleteCategory.html', category=categoryToDelete)

# Show a category items
@app.route('/weaponsGuide/<int:category_id>/')
@app.route('/weaponsGuide/<int:category_id>/items/')
def showCat(category_id):
    DBSession = sessionmaker(bind=engine)
    session = DBSession()
    categories = session.query(Categories).filter_by(id=category_id).one()
    items = session.query(CategoryItem).filter_by(
        categories_id=category_id).all()
    return render_template('weapons.html', items=items, category=categories)

# Create a new weapon
@app.route(
    '/weaponsGuide/<int:category_id>/weapon/new/', methods=['GET', 'POST'])
def newWeapon(category_id):
    DBSession = sessionmaker(bind=engine)
    session = DBSession()
    if request.method == 'POST':
        newItem = CategoryItem(name=request.form['name'], description=request.form[
                           'description'], picture=request.form['picture'], categories_id=category_id)
        session.add(newItem)
        session.commit()

        return redirect(url_for('showCat', category_id=category_id))
    else:
        return render_template('newWeapon.html', category_id=category_id)

    return render_template('newWeapon.html', category_id=category_id)

# Edit a weapon
@app.route('/weaponsGuide/<int:category_id>/weapon/<int:items_id>/edit',
           methods=['GET', 'POST'])
def editWeapon(category_id, items_id):
    DBSession = sessionmaker(bind=engine)
    session = DBSession()
    editedItem = session.query(CategoryItem).filter_by(id=items_id).one()
    if request.method == 'POST':
        if request.form['name']:
            editedItem.name = request.form['name']
        if request.form['description']:
            editedItem.description = request.form['description']
        if request.form['picture']:
            editedItem.price = request.form['picture']
        session.add(editedItem)
        session.commit()
        return redirect(url_for('showCat', category_id=category_id))
    else:

        return render_template(
            'editWeapon.html', category_id=category_id, items_id=items_id, item=editedItem)

# Delete a weapon
@app.route('/restaurant/<int:category_id>/weapon/<int:items_id>/delete',
           methods=['GET', 'POST'])
def deleteWeapon(category_id, items_id):
    DBSession = sessionmaker(bind=engine)
    session = DBSession()
    itemToDelete = session.query(CategoryItem).filter_by(id=items_id).one()
    if request.method == 'POST':
        session.delete(itemToDelete)
        session.commit()
        return redirect(url_for('showCat', category_id=category_id))
    else:
        return render_template('deleteWeapon.html', item=itemToDelete)


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
