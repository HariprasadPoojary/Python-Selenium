#           account_operation/account.py

# reach_signup
sign_up = '//a[@title="Log in to your customer account"]'
create_email_add = '//input[@id="email_create"]'
create_acc_btn = '//button[@id="SubmitCreate"]'
# already_registered
regist_email = 'email'
regist_pass = 'passwd'
regist_submit = 'SubmitLogin'
regist_acc_name = './/a[@title="View my customer account"]/span'
regist_signout = './/a[@title="Log me out"]'
# fill_details
title_mr = "uniform-id_gender1"
title_mrs = 'uniform-id_gender2'
firstname = "customer_firstname"
lastname = "customer_lastname"
email = "email"
password = "passwd"
# Date of Birth
dob_day = "days"  # selectable
dob_month = "months"  # selectable
dob_year = "years"  # selectable
# Optional check boxes
check_newsletter = "newsletter"
offers = "optin"
# Address
a_firstname = "customer_firstname"
a_lastname = "customer_lastname"
a_company = "company"
a_address1 = "address1"
a_address2 = "address2"
a_city = "city"
a_state = "id_state"  # selectable
a_postcode = "postcode"
a_additional_info = "other"
a_home_phone = "phone"
a_mobile_phone = "phone_mobile"
a_alias_address = "alias"
address_details_list = [
    a_company,
    a_address1,
    a_address2,
    a_city,
    a_state,
    a_postcode,
    a_additional_info,
    a_home_phone,
    a_mobile_phone,
    a_alias_address,
]
# Register
register_button = "submitAccount"
register_error = '//div[@id="create_account_error"]//li[contains(text(),"already been registered")]'
register_name = '//div[@class="header_user_info"]//span'

#           cart_operation/cart_operation.py

home_prod_list = '//ul[@id="homefeatured"]/li[starts-with(@class,"ajax_block_product")]'
quick_cart_prod_list = '//ul[@id="homefeatured"]/li[*]//a[@title="Add to cart"]'
quick_cart_prod_view_list = '//ul[@id="homefeatured"]/li[*]//span[text()="Quick view"]'
prod_view_add_cart = '//form[@id="buy_block"]//button[@type="submit"]'
home_cart_quantity = '//a[@title="View my shopping cart"]/span[starts-with(@class,"ajax_cart_quantity")]'
continue_shopp = '//div[@class="clearfix"]//span[@title="Continue shopping"]'
continue_shopp_close = '//div[@class="clearfix"]//span[@title="Close window"]'
