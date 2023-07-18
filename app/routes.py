from app import app

from flask import render_template, request, url_for, redirect
from .models import User, Product
from .myfunctions import Amiibo, Amiibo_all
from flask_login import current_user, login_required, login_user, logout_user

@app.route('/')
@login_required
def home():
    return render_template('home.html')

# @app.route('/products', methods=["GET", "POST"])
# @login_required
# def products():
#     if request.method == "POST":
#         # for p in Product.query.all():
#         #     if p.product_id in request.form:
#         #         product_id = p.product_id
#         #         return redirect(url_for('product', product_id=product_id))
#                     # add this to href link on html to route to product {{ url_for(product, product_id=p.id) }}
#                     pass
#     amiibos = Amiibo_all()
#     p = amiibos.request_data()
#     return render_template('products.html', p=p)

@app.route('/products')
@login_required
def products_land():
    return redirect(url_for('products', page_no=1))

@app.route('/products/<int:page_no>', methods=["GET", "POST"])
@login_required
def products(page_no=1):
    if request.method == "POST":
        pass
    amiibos = Amiibo_all()
    p = amiibos.request_data()
    start = (page_no - 1) * 12
    end = page_no *12
    return render_template('products.html', p=p, pg_start=start, pg_end=end)

@app.route('/cart')
@login_required
def cart():
    return render_template('cart.html')

@app.route('/checkout')
@login_required
def checkout():
    # if cart empty show there are no items in your cart to checkout
    return render_template('checkout.html')

@app.route('/add-product/<int:product_no>')
@login_required
def add_product(product_no):
    ### increment count of chosen product in cart
    amiibo = Amiibo(product_no)
    amiibo = amiibo.details()
    product = Product.query.filter_by(tail_id=amiibo["tail_id"]).first()
    if not product:
        return "Product not in database - Add via the add-defined-products route, or allow on the go adding"
        # print statements to check if unfound product gives None type
        print("product not in database")
        # adding products twice??? unique = False?, conditional code to add or increment product???
        # add product to Product table
        name = amiibo["name"]
        gameS = amiibo["game_series"]
        videoG = amiibo["video_game"]
        img_url = amiibo["img_url"]
        release = amiibo["release"]
        page_no = amiibo["page"]
        if amiibo["release"]:
            desc = f"Amiibo of {amiibo['name']} from the Video Game {amiibo['video_game']}, this item was released in the US on the {amiibo['release_f2']}."
        else:
            desc = f"Amiibo of {amiibo['name']} from the Video Game {amiibo['video_game']}."
        tail_id = amiibo["tail_id"]
        print(name, gameS, videoG, img_url, release, page_no, desc, tail_id, sep="\n")
        product = Product(name, gameS, videoG, img_url, release, page_no, desc, tail_id, 12.99)
        # product.addProduct()
        # print(f"product {tail_id} added!")
        # amiibo["tail_id"]
        # product = Product.query.filter_by(tail_id=amiibo["tail_id"]).first()
    
    # Add to cart
    product.add_it(current_user)
    return redirect(url_for('products', page_no=1))

@app.route('/add-defined-products/<password>')
@login_required
def add_defined_products(password):
    if password == "clutch-120":
        return "Access Granted"
        # toggle comment in/out Access Granted to enable and disable use of this function
        # this route adds defined amiibo products to the elephant sql amiibo database product table
        # use range function to define start/stop product_no for span desired to be added to product table
        # format: range(START, STOP+1) ---> if you want to add products 4 to 9 use range(4,10)
        # there are a total of 839 products in the entire api
        # currently added all products from api up to product no: 100 <--- please update this number
        tail_list = []
        for i in range(50,101):
            amiibo = Amiibo(i)
            amiibo = amiibo.details()

            name = amiibo["name"]
            gameS = amiibo["game_series"]
            videoG = amiibo["video_game"]
            img_url = amiibo["img_url"]
            release = amiibo["release"]
            page_no = amiibo["page"]
            if amiibo["release"]:
                desc = f"Amiibo of {amiibo['name']} from the Video Game {amiibo['video_game']}, this item was released in the US on the {amiibo['release_f2']}."
            else:
                desc = f"Amiibo of {amiibo['name']} from the Video Game {amiibo['video_game']}."
            tail_id = amiibo["tail_id"]

            product = Product(name, gameS, videoG, img_url, release, page_no, desc, tail_id, 12.99)
            product.addProduct()
            tail_list.append(tail_id)
            print(f"product {tail_id} added!")

        return f"Products added to database: {tail_list}"
    else:
        return "Access Denied"


@app.route('/remove-product/<int:product_id>')
@login_required
def remove_product(product_id):
    ### decrement count of chosen product in cart if it is in the cart
    # product = Product.query.get(product_id)
    # if product in current_user.added:
        # product.remove_it(current_user)
    # else:
    #     flash("You currently don't have this product in your cart")
    return redirect(url_for('product.html'))

@app.route('/clear-products/')
@login_required
def clear_products():
    ### clear all items in the cart
    # if current_user.added:
    #     for product in current_user.added:
    #         product.remove_it(current_user)
    return redirect(url_for('products.html'))

@app.route('/product/<int:product_no>')
@login_required
def product(product_no):
    amiibo = Amiibo(product_no)
    p = amiibo.details()
    # amiibo has methods .name .img_url .video_game .release etc. to use with jinja on html
    return render_template('ind-product.html', p=p)

@app.route('/contact-us')
def contact():
     return render_template('contact-us.html')

@app.route('/about-us')
def about():
     return render_template('about-us.html')
