import stripe
from datetime import datetime
from django.core.mail import send_mail
import uuid
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.csrf import csrf_exempt

from .models import *
from django.contrib import messages
from django.core.mail import EmailMessage, EmailMultiAlternatives
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.contrib.auth.models import User
from django.views.generic import ListView, CreateView, UpdateView
from django.urls import reverse_lazy
from django.conf import settings
from decimal import Decimal
from paypal.standard.forms import PayPalPaymentsForm
from datetime import date
from django.core.mail import EmailMessage, EmailMultiAlternatives

from django.core.files.storage import FileSystemStorage

from django.http import (
    HttpResponse,
    HttpResponseRedirect
)
from django.contrib.auth.forms import (
    UserChangeForm,
    PasswordChangeForm
)
from django.shortcuts import (
    render,
    redirect,
    reverse
)
from django.contrib.auth import (
    authenticate,
    login,
    logout,
    update_session_auth_hash
)
from django.utils.http import (
    urlsafe_base64_encode,
    urlsafe_base64_decode
)
from django.utils.encoding import (
    force_bytes,
    force_text
)
# Import APP Forms
from .forms import (
    loginForm,
    Suggestionform,
    Chapterform,
    Contactform,
    EditProfileForm)
from django.contrib import auth


# Create your views here.
def home(request):
    template_name = "index.html"
    slides = Slider.objects.all()
    objs = Projects.objects.all()
    teams = Team.objects.all()
    pros = Professional_Group.objects.all()
    context = {
        "index_section": True,
        "slides": slides,
        "objs": objs,
        "teams": teams,
        "pros": pros
    }
    return render(request,
                  template_name,
                  context
                  )


# Who We Are View
def who(request):
    template_name = "who.html"
    pros = Professional_Group.objects.all()
    context = {
        "who_we_are_section": True,
        "pros": pros
    }
    return render(request,
                  template_name,
                  context
                  )


# History View
def history(request):
    template_name = "history.html"
    pros = Professional_Group.objects.all()
    context = {
        "history_section": True,
        "pros": pros
    }
    return render(request,
                  template_name,
                  context
                  )


# Projects View
def projects(request):
    template_name = "projects.html"
    objs = Projects.objects.all()
    pros = Professional_Group.objects.all()
    context = {
        "teams_section": True,
        "objs": objs,
        "pros": pros
    }
    return render(request,
                  template_name,
                  context
                  )


# Project Detail View
def project_detail(request, id):
    template_name = "project_detail.html"
    obj = Projects.objects.get(id=id)
    pros = Professional_Group.objects.all()
    context = {
        "project_detail_section": True,
        "object": obj,
        "pros": pros
    }
    return render(request,
                  template_name,
                  context
                  )


# Professional Groups View
def professional_groups(request):
    template_name = "professional_groups.html"
    pros = Professional_Group.objects.all()
    context = {
        "professional_group_section": True,
        "pros": pros
    }
    return render(request,
                  template_name,
                  context
                  )


# Professional Group Detail View
def professional_detail(request, id):
    template_name = "professional_group_detail.html"
    pro = Professional_Group.objects.get(id=id)
    pros = Professional_Group.objects.all()
    context = {
        "professional_group_detail_section": True,
        "object": pro,
        "pros": pros
    }
    return render(request,
                  template_name,
                  context
                  )


# Create Local Chapter View
def LocalChapter(request):
    template_name = "create_local_chapter.html"
    pros = Professional_Group.objects.all()
    context = {
        "create_local_chapter_section": True,
        "pros": pros
    }
    return render(request,
                  template_name,
                  context
                  )


# Chapter Resources View
def ChapterResources(request):
    template_name = "chapter_resources.html"
    countries = Country.objects.all()
    pros = Professional_Group.objects.all()
    context = {
        "chapter_resources_section": True,
        "countries": countries,
        "pros": pros
    }
    return render(request,
                  template_name,
                  context
                  )


# Find Chapter View
def FindChapter(request):
    template_name = "find_a_chapter.html"
    local_chapter = Create_Chapter.objects.all()
    news = New.objects.all()
    pros = Professional_Group.objects.all()
    context = {
        "find_chapter_section": True,
        "local_chapter": local_chapter,
        "news": news,
        "pros": pros
    }
    return render(request,
                  template_name,
                  context
                  )


# Create Local Chapter View
def terms(request):
    template_name = "terms_and_conditions.html"
    pros = Professional_Group.objects.all()
    context = {
        "create_local_chapter_section": True,
        "pros": pros
    }
    return render(request,
                  template_name,
                  context
                  )


# Teams View
def teams(request):
    template_name = "teams.html"
    teams = Team.objects.all()
    pros = Professional_Group.objects.all()
    context = {
        "teams_section": True,
        "teams": teams,
        "pros": pros
    }
    return render(request,
                  template_name,
                  context
                  )


# Team Detail View
def team_detail(request, id):
    template_name = "team_detail.html"
    obj = Team.objects.get(id=id)
    pros = Professional_Group.objects.all()
    context = {
        "team_detail_section": True,
        "object": obj,
        "pros": pros
    }
    return render(request,
                  template_name,
                  context
                  )


# FAQs View
def faqs(request):
    template_name = "faqs.html"
    faqs = FAQ.objects.all()
    pros = Professional_Group.objects.all()
    context = {
        'faqs_section': True,
        'faqs': faqs,
        "pros": pros
    }
    return render(request,
                  template_name,
                  context
                  )


# Contact View
def contact(request):
    template_name = "contact_us.html"
    pros = Professional_Group.objects.all()
    form = Contactform
    if request.method == 'POST':
        form = Contactform(request.POST)
        # print(request.POST, request.FILES, sep="\n")
        print(request.POST, sep="\n")
        if form.is_valid():
            new = form.save(commit=False)
            new.save()
            form.save()
            return redirect('Index')
    context = {
        'contact_section': True,
        'form': form,
        "pros": pros
    }
    return render(request,
                  template_name,
                  context
                  )


# News View
def news(request):
    template_name = "news.html"
    news = New.objects.all()
    pros = Professional_Group.objects.all()
    context = {
        "news_section": True,
        "news": news,
        "pros": pros
    }
    return render(request,
                  template_name,
                  context
                  )


# News Detail View
def news_detail(request, id):
    template_name = "news_detail.html"
    obj = New.objects.get(id=id)
    pros = Professional_Group.objects.all()
    context = {
        "news_detail_section": True,
        "object": obj,
        "pros": pros
    }
    return render(request,
                  template_name,
                  context
                  )


# Register View
def register(request):
    template_name = "register.html"
    countries = Country.objects.all()
    groups = Professional_Group.objects.all()
    chapters = Chapter.objects.all()
    pros = Professional_Group.objects.all()
    context = {
        'register_section': True,
        'countries': countries,
        'groups': groups,
        'chapters': chapters,
        "pros": pros
    }

    if request.method == 'POST':

        country = request.POST['country']
        email = request.POST['email']
        password = request.POST['password']
        prefix = request.POST['prefix']
        first_name = request.POST['firstname']
        last_name = request.POST['lastname']
        professional = request.POST['professional']
        chapter = request.POST['chapter']

    return render(request,
                  template_name,
                  context
                  )


# Register View
def partner(request):
    template_name = "become-our-partner.html"
    countries = Country.objects.all()
    groups = Professional_Group.objects.all()
    chapters = Chapter.objects.all()
    pros = Professional_Group.objects.all()
    context = {
        'become_our_partner_section': True,
        'countries': countries,
        'groups': groups,
        'chapters': chapters,
        "pros": pros
    }

    return render(request,
                  template_name,
                  context
                  )


# Donations View
def donate(request):
    template_name = "donation.html"
    pros = Professional_Group.objects.all()
    context = {
        'donate_section': True,
        "pros": pros
    }

    return render(request,
                  template_name,
                  context
                  )


def get_chapter_fee(request):
    request.GET['']


# Login View
def login(request):
    template_name = "member_login.html"
    pros = Professional_Group.objects.all()
    if request.method != 'POST':
        form = loginForm()
    else:
        form = loginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            try:
                username = User.objects.get(email=email.lower()).username

                user = authenticate(request,
                                    username=username,
                                    password=password
                                    )
            except:
                template_name = "index.html"
                context = {
                    'dashboard_section': True,
                    'msg': 'Invalid Credentials'
                }

                return render(request,
                              template_name,
                              context
                              )
            if user is not None:
                auth.login(request,
                           user
                           )
                return redirect('Dashboard')
            else:
                messages.warning(
                    request, 'Email or password may have been entered incorrectly.')
    context = {
        'form': form,
        'login_section': True,
        "pros": pros
    }

    return render(request,
                  template_name,
                  context
                  )


# Dashboard View
@login_required
def dashboard(request):
    template_name = "dashboard/index.html"
    context = {
        'dashboard_section': True,
    }

    return render(request,
                  template_name,
                  context
                  )


def load_states(request):
    country_id = request.GET.get('country')
    states = Region.objects.filter(country_id=country_id).order_by('name')
    context = {'states': states}
    return render(request, 'dashboard/state_dropdown_list_options.html', context)


def load_cities(request):
    state_id = request.GET.get('state')
    cities = SubRegion.objects.filter(region_id=state_id).order_by('name')
    context = {'cities': cities}
    return render(request, 'dashboard/city_dropdown_list_options.html', context)


def load_chapter(request):
    chapter_name = request.GET.get('country')
    chapter_name = str(chapter_name)
    cities = Chapter.objects.filter(country=chapter_name.upper())
    print(cities)
    context = {'cities': cities}
    return render(request, 'dashboard/city_dropdown_list_options.html', context)


# Create Chapter View
@login_required
def create_chapter(request):
    template_name = "dashboard/create_chapter.html"
    form = Chapterform
    # model = Create_Chapter
    countries = Country.objects.all()

    if request.method == 'POST':
        form = Chapterform(request.POST,request.FILES)
        # print(request.POST)
        if form.is_valid():
            try:
                new = form.save(commit=False)
                new.user = request.user
                new.save()
                form.save()
                current_site = get_current_site(request)
                message = '''“Thank you for creating your chapter.
                                Your submission is under review for appropriate action,
                                we may contact you for clarifications, if necessary.
                                You will be notified once your chapter is made available for public viewing
                                and registering. Together, we will build our Nation”'''
                message += "\n\n\nFollowing is the link for the chapter review\n\n\n"
                mail_subject = 'NDF Team.'
                # build_link =  str(request.scheme) + str("://") + str( current_site.domain) + str(reverse("Petition_Details", args = [new.id]))
                # message += str(build_link)
                to_email = []
                # for i in UserProfile.objects.filter(Coverage_Admin = new.Petition_Coverage):
                #     to_email.append(str(i.user.email))
                # # print(to_email)
                approve_reject_users_email = to_email
                if not request.user.email in to_email:
                    to_email.append(request.user.email)
                send_mail(mail_subject, message,
                          "voiceitout446@gmail.com", [to_email])
            except Exception as e:
                messages.success(request, str(e))
                return redirect(reverse("Create Chapter"))
        else:
            # print("Error ache")
            # print(form.zip_code)
            print(form.errors)
            messages.success(request, str(form.errors))
            return redirect("Create Chapter")
    try:
        profile = UserProfile.objects.get(
            user=User.objects.get(username=request.user.username))
    except:
        profile = None

    context = {
        'create_chapter_section': True,
        'form': form,
        'countries': countries
    }

    return render(request,
                  template_name,
                  context
                  )


# class create_chapter:
#     model = Create_Chapter
#     form_class = Chapterform
#     success_url = reverse_lazy('Dashboard')


# Suggestion View
@login_required
def suggestion(request):
    template_name = "dashboard/suggestion.html"
    form = Suggestionform()
    msg = ''
    if request.method == 'POST':
        form = Suggestionform(request.POST)
        # print(request.POST, request.FILES, sep="\n")
        print(request.POST, sep="\n")
        if form.is_valid():
            new = form.save(commit=False)
            new.user = request.user
            new.save()
            form.save()
            msg = 'Your suggestion is successfully sent'
            return redirect('Dashboard')
    context = {
        'form': form,
        'suggestion_section': True,
        'msg': msg
    }

    return render(request,
                  template_name,
                  context
                  )


# Project Support View
def support(request):
    template_name = "dashboard/supports.html"

    proj = project_support.objects.filter(user=request.user).last()
    if not proj:
        st_proj = datetime.now().date()
        end_proj = datetime.now().date()
    else:
        st_proj = proj.start_date
        end_proj = proj.end_date

    try:
        memb = membership.objects.filter(user=request.user).last()

        if not memb:
            msg = 'You are not registered'
            template_name = 'register.html'
            countries = Country.objects.all()
            groups = Professional_Group.objects.all()
            chapters = Chapter.objects.all()
            context = {
                'register_section': True,
                'countries': countries,
                'groups': groups,
                'chapters': chapters,
                'msg': msg
            }

            return render(request,
                          template_name,
                          context
                          )
        else:
            st_mem = memb.start_date
            end_mem = memb.end_date
            chapter = Chapter.objects.get(name=memb.chapter)
            fee = chapter.fee

    except membership.DoesNotExist:
        return redirect('Join NDF')

    context = {
        'support_section': True,
        'st_proj': st_proj,
        'end_proj': end_proj,
        'st_mem': st_mem,
        'end_mem': end_mem,
        'fee': fee
    }

    return render(request,
                  template_name,
                  context
                  )


# Purchase Vouchers View
def vouchers(request):
    template_name = "dashboard/vouchers.html"
    countries = Chapter.objects.all()
    g_vouchers = Voucher.objects.filter(
        used_by=request.user, voucher_type="GeneralVoucher").order_by("status")
    c_vouchers = Voucher.objects.filter(
        used_by=request.user, voucher_type="CountryVoucher").order_by("status")
    context = {
        'vouchers_section': True,
        'countries': countries,
        'g_vouchers': g_vouchers,
        'c_vouchers': c_vouchers

    }

    return render(request,
                  template_name,
                  context
                  )


# Donations View
def donation(request):
    template_name = "dashboard/donation.html"
    context = {
        'donations_section': True,
    }

    return render(request,
                  template_name,
                  context
                  )


# Profile View
def profile(request):
    template_name = "dashboard/profile.html"

    context = {
        'profile_section': True,
    }
    if request.method == 'POST' and request.FILES['image']:

        profile_obj = UserProfile_new()
        fs = FileSystemStorage()

        if UserProfile_new.objects.filter(user=request.user).exists():
            profile_obj = UserProfile_new.objects.filter(user=request.user)
            profile_obj.update(first_name=request.POST['first_name'])
            profile_obj.update(last_name=request.POST['last_name'])
            profile_obj.update(street_address=request.POST['street_address'])
            profile_obj.update(postal_code=request.POST['postal_code'])
            profile_obj.update(country=request.POST['country'])
            profile_obj.update(state=request.POST['state'])
            profile_obj.update(city=request.POST['city'])
            profile_obj.update(email=request.POST['email'])
            profile_obj.update(dob=request.POST['dob'])
            profile_obj.update(phone=request.POST['phone'])

            image_file = request.FILES['image']
            file_save = fs.save(image_file.name, image_file)
            uploaded_file_url = fs.url(file_save)
            profile_obj.update(image=image_file)

            return redirect('/')

        else:
            profile_obj.user = request.user
            profile_obj.first_name = request.POST['first_name']
            profile_obj.last_name = request.POST['last_name']
            profile_obj.street_address = request.POST['street_address']
            profile_obj.postal_code = request.POST['postal_code']
            profile_obj.country = request.POST['country']
            profile_obj.state = request.POST['state']
            profile_obj.city = request.POST['city']
            profile_obj.email = request.POST['email']
            profile_obj.dob = request.POST['dob']
            profile_obj.phone = request.POST['phone']
            image_file = request.FILES['image']
            file_save = fs.save(image_file.name, image_file)
            uploaded_file_url = fs.url(file_save)
            profile_obj.image = image_file

            profile_obj.save()

            return redirect('/')

    return render(request,
                  template_name,
                  context
                  )


# Change Password View
def change_password(request):
    # template_name = "dashboard/change_password.html"
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(
                request, 'Your password was successfully updated!')
            return redirect('change_password')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'dashboard/change_password.html', {
        'form': form,
        'change_password_section': True
    })


# Invite Friends View
import re
regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
# import json


# Invite Friends Viewimport json

def invite_friends(request):
    template_name = "dashboard/invite_friends.html"
    context = {
        'invite_friends_section': True,

    }
    users = User.objects.all()
    users_email = []

    for user in users:
        users_email.append(user.email)
# Validate the email
    if request.method == 'POST':
        email = request.POST['email']
        if not (re.search(regex,email)):
          msg = 'Invalid Email'
          context = {'dashboard_section': True,'msg': msg}
          return render(request,'dashboard/index.html',context)

        if email in users_email:
          msg = 'msg'
          context = {'dashboard_section': True,'msg': msg}
          return render(request,'dashboard/invite_friends.html',context)


        if request.POST['code'] == '':
            print("sending email without voucher.......")

            send_mail(
                'NDF',
                "Invite",
                settings.EMAIL_ADMIN,
                [request.POST['email']],
                html_message="Hello, Your are being invited to join NDF by " + request.user.email + "\nClick <a href='https://greatnigerian.org/'>https://greatnigerian.org/</a> to join."
            );
            context = {
                'invite_friends_section': True,
                'msg': 'Invite Sent'
            }
            return render(request,
                          template_name,
                          context
                          )

        elif Voucher.objects.filter(voucher_code=request.POST['code']).exists() and Voucher.objects.filter(voucher_code=request.POST['code'], status='Okay') and Voucher.objects.filter(voucher_code=request.POST['code'], used_by= request.user):

            v_code = request.POST['code']
            v_obj = Voucher.objects.get(voucher_code=v_code)

            v_uses_obj = Voucher_uses()

            v_uses_obj.Voucher_obj = v_obj
            v_uses_obj.used_by = request.user
            v_uses_obj.used_to = request.POST['email']
            v_uses_obj.save()
            Voucher.objects.filter(voucher_code=request.POST['code']).update(status='Used')


            print("sending email with voucher.......")
            print(settings.EMAIL_ADMIN)

            code = request.POST['code']
            print(code)
            print(request.POST['email'])

            # msg = EmailMultiAlternatives("Subject", "Hello, Your are being invited to join NDF by " + request.user.email + "\nClick on http://127.0.0.1:8000/ to join. Your registeration voucher code is:"+code, settings.EMAIL_ADMIN, [request.POST['email']])
            # msg.attach_alternative("Hello, Your are being invited to join NDF by " + request.user.email + "\nClick on http://127.0.0.1:8000/ to join. Your registeration voucher code is:"+code, "text/html")
            # msg.send()
            send_mail(
                'NDF',
                "Invite",
                settings.EMAIL_ADMIN,
                [request.POST['email']],
                html_message="Hello, Your are being invited to join NDF by " + request.user.email + "\nClick on http://127.0.0.1:8000/ to join. Your registeration voucher code is:" + code
            );
            print("Sent Invite")
            context = {
                'invite_friends_section': True,
                'msg': 'Invite Sent'
            }
            return render(request,
                          template_name,
                          context,

                          )

        else: # display error if voucher used or invalid
            msg = 'Voucher Code Is Used Or Invalid'
            context = {'dashboard_section': True,'msg': msg}
            return render(request,'dashboard/index.html',context)

    return render(request,
                  template_name,
                  context
                  )

def endorse_member(request):
    try:
        myuser = endorsement.objects.filter(user=request.user)
        myendorsements = []
        for x in myuser:
            myendorsements.append(x.endorsed_by)
    except endorsement.DoesNotExist:
        myendorsements = ''
    if request.method == "POST":
        email = request.POST['email']
        try:
            user = User.objects.get(email=email)
        except:
            msg = 'User you want to endorse does not exist'

            context = {
                'dashboard_section': True,
                'msg': msg
            }

            return render(request,
                          "dashboard/index.html",
                          context
                          )
        endorsing_user = request.user
        if endorsement.objects.filter(user=user, endorsed_by=endorsing_user).exists():
            msg = 'This endorsement already exists.'
            context = {'dashboard_section': True, 'msg': msg}
            return render(request, "dashboard/index.html", context)
        if user == endorsing_user:
            msg = 'This user cannot be endorsed.'
            context = {'dashboard_section': True, 'msg': msg}
            return render(request, "dashboard/index.html", context)

        member = endorsement.objects.create(
            user=user, endorsed_by=endorsing_user)
        member.save()
        return render(request, 'dashboard/endorse_member.html', {'myendorsements': myendorsements, 'msg': 'sent'})
    return render(request, 'dashboard/endorse_member.html', {'myendorsements': myendorsements})


def process_payment(request):
    voucher_type = request.POST['type']
    amount = float(request.POST['country'])
    quantity = int(request.POST['quantity'])
    print(amount, "----------------- Q=", quantity)
    total_amount = amount * quantity

    host = request.get_host()
    template = ''
    return_template = ''
    context = {}
    paypal_dict = {}
    user = request.user
    print(request.POST['payment_method'])
    if request.POST['payment_method'] == 'Not':
        total_amount = amount * quantity
        paypal_dict = {
            # 'voucher_type':voucher_type,
            'quantity': quantity,
            'business': settings.PAYPAL_RECEIVER_EMAIL,
            'unit_item': amount,
            'item_number': 1,
            'item_name': voucher_type,
            'amount': amount,
            # 'invoice': str(amount),
            'currency_code': 'USD',
            'notify_url': 'http://{}{}'.format(host,
                                               reverse('paypal-ipn')),
            'return': 'http://{}{}'.format(host,
                                           reverse('payment_done')),
            'cancel_return': 'http://{}{}'.format(host,
                                                  reverse('payment_cancelled')),
            'image': 'http://www.paypal.com/en_US/i/btn/x-click-but01.gif',
            'rm': 2,
            'charset': "utf-8",

        }
        template = 'paypal/process_payment.html'

    if request.POST['payment_method'] == 'Paypal':
        if User.objects.filter(username=request.POST['firstname']).exists():
            msg = 'Username or email already exists'
            countries = Country.objects.all()
            groups = Professional_Group.objects.all()
            chapters = Chapter.objects.all()
            context = {
                'register_section': True,
                'countries': countries,
                'groups': groups,
                'chapters': chapters,
                'msg': msg

            }

            return render(request,
                          "register.html",
                          context
                          )
        if User.objects.filter(username=request.POST['email']).exists():
            msg = 'Username or email already exists'
            countries = Country.objects.all()
            groups = Professional_Group.objects.all()
            chapters = Chapter.objects.all()
            context = {
                'register_section': True,
                'countries': countries,
                'groups': groups,
                'chapters': chapters,
                'msg': msg

            }

            return render(request,
                          "register.html",
                          context
                          )
        template = 'paypal/paypal_payment.html'
        if request.POST['object_type'] == 'Membership':
            res_country = request.POST['res_country']
            email = request.POST['email']
            password = request.POST['password']
            first_name = request.POST['firstname']
            last_name = request.POST['lastname']
            professional = request.POST['professional']
            chapter = request.POST['type']
            print("++++++++++++++++++++++++++++++++++++++++++++")
            print("I am here.....")
            print("++++++++++++++++++++++++++++++++++++++++++++")
            return_template = ''
            objectstring = voucher_type + ',' + first_name + ',' + last_name + \
                ',' + res_country + ',' + email + ',' + password + ',' + professional
            paypal_dict = {
                # 'voucher_type':voucher_type,
                'quantity': quantity,
                'res_country': res_country,
                'email': email,
                'password': password,
                'first_name': first_name,
                'last_name': last_name,
                'professional': professional,
                'chapter': chapter,
                'business': settings.PAYPAL_RECEIVER_EMAIL,
                'unit_item': amount,
                'item_number': 1,
                'item_name': objectstring,
                'amount': amount,
                # 'invoice': str(amount),
                'currency_code': 'USD',
                'notify_url': 'http://{}{}'.format(host,
                                                   reverse('paypal-ipn')),
                'return': 'http://{}{}'.format(host,
                                               reverse('payment_done_membership')),
                'cancel_return': 'http://{}{}'.format(host,
                                                      reverse('payment_cancelled')),
                'image': 'http://www.paypal.com/en_US/i/btn/x-click-but01.gif',
                'rm': 2,
                'charset': "utf-8",

            }

        if request.POST['object_type'] == 'Membership_renew':
            return_template = 'payment_done_membership_renew'
            paypal_dict = {
                # 'voucher_type':voucher_type,
                'quantity': quantity,
                'business': settings.PAYPAL_RECEIVER_EMAIL,
                'unit_item': amount,
                'item_number': 1,
                'item_name': voucher_type,
                'amount': amount,
                # 'invoice': str(amount),
                'currency_code': 'USD',
                'notify_url': 'http://{}{}'.format(host,
                                                   reverse('paypal-ipn')),
                'return': 'http://{}{}'.format(host,
                                               reverse('payment_done_membership_renew')),
                'cancel_return': 'http://{}{}'.format(host,
                                                      reverse('payment_cancelled')),
                'image': 'http://www.paypal.com/en_US/i/btn/x-click-but01.gif',
                'rm': 2,
                'charset': "utf-8",

            }

        if request.POST['object_type'] == 'Project_support':
            return_template = 'payment_done_project_support'
            package = request.POST['package']
            upgrade = request.POST['upgrade']
            objectstring = voucher_type + ',' + package + ',' + upgrade
            paypal_dict = {
                # 'voucher_type':voucher_type,
                'quantity': quantity,
                'package': package,
                'business': settings.PAYPAL_RECEIVER_EMAIL,
                'unit_item': amount,
                'item_number': 1,
                'item_name': objectstring,
                'amount': amount,
                'upgrade': upgrade,
                # 'invoice': str(amount),
                'currency_code': 'USD',
                'notify_url': 'http://{}{}'.format(host,
                                                   reverse('paypal-ipn')),
                'return': 'http://{}{}'.format(host,
                                               reverse('payment_done_project_support')),
                'cancel_return': 'http://{}{}'.format(host,
                                                      reverse('payment_cancelled')),
                'image': 'http://www.paypal.com/en_US/i/btn/x-click-but01.gif',
                'rm': 2,
                'charset': "utf-8",

            }

        if request.POST['object_type'] == 'Donation':
            return_template = 'payment_done_donation'
            frequency = request.POST['frequency']
            duration = request.POST['duration']
            first_name = request.POST['firstname']
            last_name = request.POST['lname']
            address = request.POST['address1']
            postal_code = request.POST['postal_code']
            res_country = request.POST['res_country']
            email = request.POST['email']
            city = request.POST['city']
            state = request.POST['state']
            objectstring = voucher_type + ',' + first_name + ',' + last_name + ',' + res_country + ',' + email + \
                ',' + frequency + ',' + duration + ',' + address + \
                ',' + postal_code + ',' + city + ',' + state
            # if frequency == 'weekly':
            #     price = amount
            #     billing_cycle = 1
            #     billing_cycle_unit = "W"
            # if frequency == 'monthly':
            #     price = amount
            #     billing_cycle = 1
            #     billing_cycle_unit = "M"
            # if frequency == 'quarterly':
            #     price = amount
            #     billing_cycle = 1
            #     billing_cycle_unit = "Y"
            # if frequency == 'twice a year':
            #     price = amount
            #     billing_cycle = 2
            #     billing_cycle_unit = "Y"
            # if frequency == 'yearly':
            #     price = amount
            #     billing_cycle = 1
            #     billing_cycle_unit = "Y"
            paypal_dict = {
                # 'voucher_type':voucher_type,
                # "cmd": "_xclick-subscriptions",
                # "a3": price,  # monthly price
                # "p3": billing_cycle,  # duration of each unit (depends on unit)
                # "t3": billing_cycle_unit,  # duration unit ("M for Month")
                # "src": "1",  # make payments recur
                'quantity': quantity,
                'res_country': res_country,
                'email': email,
                'first_name': first_name,
                'last_name': last_name,
                'postal_code': postal_code,
                'frequency': frequency,
                'duration': duration,
                'address': address,
                'city': city,
                'state': state,
                'business': settings.PAYPAL_RECEIVER_EMAIL,
                'unit_item': amount,
                'item_number': 1,
                'item_name': objectstring,
                'amount': amount,
                # 'invoice': str(amount),
                'currency_code': 'USD',
                'notify_url': 'http://{}{}'.format(host,
                                                   reverse('paypal-ipn')),
                'return': 'http://{}{}'.format(host,
                                               reverse('payment_done_donation')),
                'cancel_return': 'http://{}{}'.format(host,
                                                      reverse('payment_cancelled')),
                'image': 'http://www.paypal.com/en_US/i/btn/x-click-but01.gif',
                'rm': 2,
                'charset': "utf-8",

            }

    if request.POST['payment_method'] == 'Stripe':
        if request.POST['object_type'] == 'Membership':
            if User.objects.filter(username=request.POST['firstname']).exists():
                msg = 'Username or email already exists'
                countries = Country.objects.all()
                groups = Professional_Group.objects.all()
                chapters = Chapter.objects.all()
                context = {'register_section': True, 'countries': countries, 'groups': groups, 'chapters': chapters,
                           'msg': msg}
                return render(request, "register.html", context)
            if User.objects.filter(username=request.POST['email']).exists():
                msg = 'Username or email already exists'
                countries = Country.objects.all()
                groups = Professional_Group.objects.all()
                chapters = Chapter.objects.all()
                context = {'register_section': True, 'countries': countries, 'groups': groups, 'chapters': chapters,
                           'msg': msg}

                return render(request, "register.html", context)
            res_country = request.POST['res_country']
            email = request.POST['email']
            password = request.POST['password']
            first_name = request.POST['firstname']
            last_name = request.POST['lastname']
            professional = request.POST['professional']
            chapter = request.POST['type']
            total_amount = total_amount * 100
            context = {
                'res_country': res_country,
                'email': email,
                'password': password,
                'first_name': first_name,
                'last_name': last_name,
                'professional': professional,
                'chapter': chapter
            }
            template = 'paypal/stripe_payment_membership.html'
            return_template = 'payment_done_membership'
        if request.POST['object_type'] == 'Membership_renew':
            context = {

            }
            total_amount = total_amount * 100
            template = 'paypal/stripe_payment_membership_renew.html'
            return_template = 'payment_done_membership'
        if request.POST['object_type'] == 'Project_support':
            package = request.POST['package']
            upgrade = request.POST['upgrade']
            total_amount = total_amount * 100
            context = {
                'package': package,
                'upgrade': upgrade
            }
            template = 'paypal/stripe_payment_project_support.html'
            return_template = 'payment_done_membership'
        if request.POST['object_type'] == 'Donation':
            frequency = request.POST['frequency']
            duration = request.POST['duration']
            first_name = request.POST['firstname']
            last_name = request.POST['lname']
            address = request.POST['address1']
            postal_code = request.POST['postal_code']
            res_country = request.POST['res_country']
            email = request.POST['email']
            city = request.POST['city']
            state = request.POST['state']
            total_amount = total_amount * 100
            context = {
                'res_country': res_country,
                'email': email,
                'first_name': first_name,
                'last_name': last_name,
                'postal_code': postal_code,
                'frequency': frequency,
                'duration': duration,
                'address': address,
                'city': city,
                'state': state
            }
            template = 'paypal/stripe_payment_donation.html'
            return_template = 'payment_done_membership'
        if request.POST['object_type'] == 'Donationn':
            frequency = request.POST['frequency']
            duration = request.POST['duration']
            first_name = request.POST['firstname']
            last_name = request.POST['lname']
            address = request.POST['address1']
            postal_code = request.POST['postal_code']
            res_country = request.POST['res_country']
            email = request.POST['email']
            city = request.POST['city']
            state = request.POST['state']
            total_amount = total_amount * 100
            context = {
                'res_country': res_country,
                'email': email,
                'first_name': first_name,
                'last_name': last_name,
                'postal_code': postal_code,
                'frequency': frequency,
                'duration': duration,
                'address': address,
                'city': city,
                'state': state
            }
            template = 'paypal/stripe_payment_donationn.html'
            return_template = 'payment_done_membership'

    if request.POST['payment_method'] == 'Voucher':

        voucher_code = request.POST['voucher']
        if voucher_code == '':
            msg = 'Voucher Code is empty please enter it first'
            if not request.user.is_authenticated:
                countries = Country.objects.all()
                groups = Professional_Group.objects.all()
                chapters = Chapter.objects.all()
                context = {
                    'register_section': True,
                    'countries': countries,
                    'groups': groups,
                    'chapters': chapters,
                    'msg': msg
                }

                return render(request,
                              "register.html",
                              context
                              )
            else:
                context = {
                    'donations_section': True,
                    'msg': msg
                }

                return render(request,
                              'dashboard/index.html',
                              context
                              )

        try:
            vouch = Voucher.objects.get(voucher_code=voucher_code)
        except:
            msg = 'Voucher Code is invalid'
            if not request.user.is_authenticated:
                countries = Country.objects.all()
                groups = Professional_Group.objects.all()
                chapters = Chapter.objects.all()
                context = {
                    'register_section': True,
                    'countries': countries,
                    'groups': groups,
                    'chapters': chapters,
                    'msg': msg
                }

                return render(request,
                              "register.html",
                              context
                              )
            else:
                context = {
                    'donations_section': True,
                    'msg': msg
                }

                return render(request,
                              'dashboard/index.html',
                              context
                              )

        if vouch.status == 'Used':
            print("here at join ndf")
            msg = 'Sorry this Voucher is previously used'
            if not request.user.is_authenticated:
                countries = Country.objects.all()
                groups = Professional_Group.objects.all()
                chapters = Chapter.objects.all()
                context = {
                    'register_section': True,
                    'countries': countries,
                    'groups': groups,
                    'chapters': chapters,
                    'msg': msg
                }

                return render(request,
                              "register.html",
                              context
                              )
            else:
                context = {
                    'donations_section': True,
                    'msg': msg
                }

                return render(request,
                              'dashboard/index.html',
                              context
                              )

        if vouch.amount < total_amount:
            print("here at join ndf")
            msg = 'Your Voucher amount is not enough for this purchase'
            if not request.user.is_authenticated:
                countries = Country.objects.all()
                groups = Professional_Group.objects.all()
                chapters = Chapter.objects.all()
                context = {
                    'register_section': True,
                    'countries': countries,
                    'groups': groups,
                    'chapters': chapters,
                    'msg': msg

                }

                return render(request,
                              "register.html",
                              context
                              )
            else:
                context = {
                    'donations_section': True,
                    'msg': msg
                }

                return render(request,
                              'dashboard/index.html',
                              context
                              )

        template = 'paypal/paypal_payment.html'
        return_template = 'payment_done_membership'
        if request.POST['object_type'] == 'Membership':
            if User.objects.filter(username=request.POST['firstname']).exists():
                msg = 'Username or email already exists'
                countries = Country.objects.all()
                groups = Professional_Group.objects.all()
                chapters = Chapter.objects.all()
                context = {'register_section': True, 'countries': countries, 'groups': groups, 'chapters': chapters,
                           'msg': msg}
                return render(request, "register.html", context)
            if User.objects.filter(username=request.POST['email']).exists():
                msg = 'Username or email already exists'
                countries = Country.objects.all()
                groups = Professional_Group.objects.all()
                chapters = Chapter.objects.all()
                context = {
                    'register_section': True,
                    'countries': countries,
                    'groups': groups,
                    'chapters': chapters,
                    'msg': msg

                }

                return render(request,
                              "register.html",
                              context
                              )
            vouch.amount = float(vouch.amount) - total_amount
            vouch.status = 'Used'
            vouch.used_time = datetime.now()
            vouch.save()
            print("here at index")
            res_country = request.POST['res_country']
            email = request.POST['email']
            password = request.POST['password']
            first_name = request.POST['firstname']
            last_name = request.POST['lastname']
            professional = request.POST['professional']
            chapter = request.POST['type']
            try:
                user = User.objects.create_user(
                    username=first_name, email=email, password=password)
                user.save()
            except:
                msg = 'Username or email already exists'
                countries = Country.objects.all()
                groups = Professional_Group.objects.all()
                chapters = Chapter.objects.all()
                context = {
                    'register_section': True,
                    'countries': countries,
                    'groups': groups,
                    'chapters': chapters,
                    'msg': msg

                }

                return render(request,
                              "register.html",
                              context
                              )
            auth.login(request, user)
            # charge = stripe.Charge.create(
            #     amount=amount_temp,
            #     currency='usd',
            #     description=voucher_type,
            #     source=request.POST['stripeToken']
            # )
            d_now = date.today()
            d_now = d_now.replace(year=d_now.year + 1)
            member = membership.objects.create(chapter=chapter, first_name=first_name, last_name=last_name,
                                               country=res_country, email=email, professional_group=professional,
                                               user=user, start_date=datetime.now().date(), end_date=d_now)
            member.save()
            send_mail(
                'NDF',
                "Membership Registration",
                settings.EMAIL_ADMIN,
                [email],
                html_message="Congratulations!, Your are registered as a member<br>Your professional group is: " + str(
                    member.professional_group) + ", Chapter name is : " + str(
                    member.chapter) + " and member ID is : " + str(
                    member.id) + " "
            )
            msg = 'Your are registered!'

            context = {
                'dashboard_section': True,
                'msg': msg
            }

            return render(request,
                          "dashboard/index.html",
                          context
                          )

        if request.POST['object_type'] == 'Membership_renew':
            vouch.amount = float(vouch.amount) - total_amount
            vouch.status = 'Used'
            vouch.used_time = datetime.now()
            vouch.save()
            print("here at index")
            user = request.user
            member = membership.objects.get(user=user, email=user.email)
            d_now = member.end_date
            d_now = d_now.replace(year=d_now.year + 1)
            member.end_date = d_now
            member.save()
            send_mail(
                'NDF',
                "Membership Renewed",
                settings.EMAIL_ADMIN,
                [user.email],
                html_message="Congratulations!, Your membership is renewed"
            )
            msg = 'Your membership is renewed'

            context = {
                'dashboard_section': True,
                'msg': msg
            }

            return render(request,
                          "dashboard/index.html",
                          context
                          )
        if request.POST['object_type'] == 'Project_support':

            print("here at index")
            package = request.POST['package']

            amount_temp = float(request.POST['country'])
            quantity = int(request.POST['quantity'])
            amount = amount_temp / quantity

            upgrade = request.POST['upgrade']
            user = request.user
            d_now = date.today()
            d_now = d_now.replace(year=d_now.year + 1)

            if upgrade == 'no':
                project = project_support.objects.create(package=package, paid_amount=amount_temp, user=user,
                                                         start_date=datetime.now().date(), end_date=d_now)
                send_mail(
                    'NDF',
                    "Project Support",
                    settings.EMAIL_ADMIN,
                    [user.email],
                    html_message="Congratulations!, Project support created"
                )

            else:

                try:
                    project = project_support.objects.get(user=user)
                except:
                    context = {
                        'donations_section': True,
                        'msg': 'There is no such Project Support.'
                    }

                    return render(request,
                                  'dashboard/index.html',
                                  context
                                  )
                d_now = project.end_date
                d_now = d_now.replace(year=d_now.year + 1)
                project.end_date = d_now
                project.paid_amount = amount_temp
                send_mail(
                    'NDF',
                    "Project Support Renewed",
                    settings.EMAIL_ADMIN,
                    [user.email],
                    html_message="Congratulations!, Project support Renewed"
                )
            project.save()
            vouch.amount = float(vouch.amount) - total_amount
            vouch.status = 'Used'
            vouch.used_time = datetime.now()
            vouch.save()
            msg = 'Successful!'

            context = {
                'dashboard_section': True,
                'msg': msg
            }

            return render(request,
                          "dashboard/index.html",
                          context
                          )
        if request.POST['object_type'] == 'Donation':
            vouch.amount = float(vouch.amount) - total_amount
            vouch.status = 'Used'
            vouch.used_time = datetime.now()
            vouch.save()
            print("here at index")
            print("hellloooooooooooooo I am here")
            frequency = request.POST['frequency']
            duration = request.POST['duration']
            first_name = request.POST['firstname']
            last_name = request.POST['lname']
            address = request.POST['address1']
            postal_code = request.POST['postal_code']
            res_country = request.POST['res_country']
            email = request.POST['email']
            city = request.POST['city']
            state = request.POST['state']
            donate = donations.objects.create(frequency=frequency, duration=duration, donating_amount=voucher_type,
                                              paid_amount=amount, first_name=first_name,
                                              last_name=last_name, street_address=address,
                                              postal_code=postal_code,
                                              country=res_country, state=state, city=city, email=email,
                                              user=user)
            donate.save()
            send_mail(
                'NDF',
                "Donation",
                settings.EMAIL_ADMIN,
                [email],
                html_message="Congratulations!, Your donation is successful."
            )
            msg = 'Your donation is successful.'

            context = {
                'dashboard_section': True,
                'msg': msg
            }

            return render(request,
                          "dashboard/index.html",
                          context
                          )

        if request.POST['object_type'] == 'Donationn':
            vouch.amount = float(vouch.amount) - total_amount
            vouch.status = 'Used'
            vouch.used_time = datetime.now()
            vouch.save()
            print("here at index")
            print("hellloooooooooooooo I am here")
            frequency = request.POST['frequency']
            duration = request.POST['duration']
            first_name = request.POST['firstname']
            last_name = request.POST['lname']
            address = request.POST['address1']
            postal_code = request.POST['postal_code']
            res_country = request.POST['res_country']
            email = request.POST['email']
            city = request.POST['city']
            state = request.POST['state']
            donate = donations.objects.create(frequency=frequency, duration=duration, donating_amount=voucher_type,
                                              paid_amount=amount, first_name=first_name,
                                              last_name=last_name, street_address=address,
                                              postal_code=postal_code,
                                              country=res_country, state=state, city=city, email=email,
                                              user=user)
            donate.save()
            send_mail(
                'NDF',
                "Donation",
                settings.EMAIL_ADMIN,
                [email],
                html_message="Congratulations!, Your donation is successful."
            )
            msg = 'Your donation is successful.'

            context = {
                'dashboard_section': True,
                'msg': msg
            }

            return render(request,
                          "index.html",
                          context
                          )

    form = PayPalPaymentsForm(initial=paypal_dict)
    stripe_key = settings.STRIPE_PUBLISHABLE_KEY
    stripe_amount = total_amount * 100
    return render(request, template_name=template,
                  context={'form': form, 'stripe_key': stripe_key, 'total_amount': total_amount,
                           'voucher_type': voucher_type, 'quantity': quantity, 'context': context,
                           'stripe_amount': stripe_amount})


def process_payment_membership(request):
    voucher_type = request.POST['type']
    amount = float(request.POST['country'])
    quantity = int(request.POST['quantity'])
    print(amount, "----------------- Q=", quantity)
    total_amount = amount * quantity
    host = request.get_host()

    paypal_dict = {
        # 'voucher_type':voucher_type,
        'quantity': quantity,

        'business': settings.PAYPAL_RECEIVER_EMAIL,
        'unit_item': amount,
        'item_number': 1,
        'item_name': voucher_type,
        'amount': amount,
        # 'invoice': str(amount),
        'currency_code': 'USD',
        'notify_url': 'http://{}{}'.format(host,
                                           reverse('paypal-ipn')),
        'return': 'http://{}{}'.format(host,
                                       reverse('payment_done')),
        'cancel_return': 'http://{}{}'.format(host,
                                              reverse('payment_cancelled')),
        'image': 'http://www.paypal.com/en_US/i/btn/x-click-but01.gif',
        'rm': 2,
        'charset': "utf-8",

    }

    form = PayPalPaymentsForm(initial=paypal_dict)
    stripe_key = settings.STRIPE_PUBLISHABLE_KEY
    template = ''
    print(request.POST['payment_method'])
    if request.POST['payment_method'] == 'Not':
        template = 'paypal/process_payment.html'
    if request.POST['payment_method'] == 'Paypal':
        template = 'paypal/paypal_payment.html'
    if request.POST['payment_method'] == 'Stripe':
        template = 'paypal/stripe_payment_membership_renew.html'
    if request.POST['payment_method'] == 'Voucher':
        template = ''

    return render(request, template_name='',
                  context={'form': form, 'stripe_key': stripe_key, 'total_amount': total_amount,
                           'voucher_type': voucher_type, 'quantity': quantity})


@csrf_exempt
def payment_done(request):
    voucher_type = request.POST['item_name']
    amount_temp = float(request.POST['mc_gross'])
    quantity = int(request.POST['quantity'])
    amount = amount_temp / quantity
    if request.user.is_authenticated is None:
        return HttpResponse("USER NOT FOUND")

    user = request.user
    for i in range(0, quantity):
        while 1:
            code = str(uuid.uuid4().int)[:16]
            t = iter(code)
            voucher_code = "-".join(a + b + c + d for a,
                                    b, c, d in zip(t, t, t, t))
            voucher_codes = Voucher.objects.all()
            unique = True
            for vouch in voucher_codes:
                if voucher_code == vouch.voucher_code:
                    unique = False

            if unique == True:
                break
        v = Voucher.objects.create(voucher_code=voucher_code, voucher_type=voucher_type, amount=amount,
                                   purchase_time=datetime.now(), used_by=user)
        v.save()
        send_mail(
            'NDF',
            " ",
            settings.EMAIL_ADMIN,
            [request.user.email],
            html_message="Your NDF Voucher of type <b>" + voucher_type +
            "</b> has been created Successfully.<br> Your voucher code is <h3>" +
            voucher_code + ".</h3>"
        )
        send_mail(
            'NDF',
            " ",
            settings.EMAIL_ADMIN,
            [settings.EMAIL_ADMIN],
            html_message="An NDF Voucher of type <b>" + voucher_type + "</b> has been created by User <b>" +
            request.user.email + "</b>.<br>Voucher code is <h3>" + voucher_code + ".</h3>"
        )

    return render(request, 'paypal/payment_done.html')


@csrf_exempt
def payment_done_membership(request):
    item = request.POST['item_name1']
    amount_temp = float(request.POST['mc_gross'])
    item = item.split(',')
    chapter = item[0]
    first_name = item[1]
    last_name = item[2]
    country = item[3]
    email = item[4]
    password = item[5]
    try:
        user = User.objects.create_user(
            username=first_name, email=email, password=password)
        user.save()
    except:
        msg = 'Username or email already exists'
        countries = Country.objects.all()
        groups = Professional_Group.objects.all()
        chapters = Chapter.objects.all()
        context = {
            'register_section': True,
            'countries': countries,
            'groups': groups,
            'chapters': chapters,
            'msg': msg

        }

        return render(request,
                      "register.html",
                      context
                      )
    auth.login(request, user)

    professional = item[6]

    quantity = int(request.POST['quantity1'])
    amount = amount_temp / quantity

    # charge = stripe.Charge.create(
    #     amount=amount_temp,
    #     currency='usd',
    #     description=voucher_type,
    #     source=request.POST['stripeToken']
    # )
    d_now = date.today()
    d_now = d_now.replace(year=d_now.year + 1)
    member = membership.objects.create(chapter=chapter, first_name=first_name, last_name=last_name,
                                       country=country, email=email, professional_group=professional,
                                       user=user, start_date=datetime.now().date(), end_date=d_now)
    member.save()
    send_mail(
        'NDF',
        "Membership Registration",
        settings.EMAIL_ADMIN,
        [email],
        html_message="Congratulations!, Your are registered as a member"
    )
    return render(request, 'paypal/payment_done.html')


@csrf_exempt
def payment_done_membership_renew(request):
    user = request.user
    member = membership.objects.filter(user=user, email=user.email).last()
    d_now = member.end_date
    d_now = d_now.replace(year=d_now.year + 1)
    member.end_date = d_now
    member.save()
    send_mail(
        'NDF',
        "Membership Renewed",
        settings.EMAIL_ADMIN,
        [user.email],
        html_message="Congratulations!, Your membership is renewed"
    )

    return render(request, 'paypal/payment_done.html')


@csrf_exempt
def payment_done_project_support(request):
    item = request.POST['item_name1']
    item = item.split(',')
    amount_temp = float(request.POST['mc_gross'])
    quantity = int(request.POST['quantity1'])
    amount = amount_temp / quantity
    user = request.user
    upgrade = item[2]
    package = item[1]
    d_now = date.today()
    d_now = d_now.replace(year=d_now.year + 1)
    if upgrade == 'no':
        project = project_support.objects.create(package=package, paid_amount=amount_temp, user=user,
                                                 start_date=datetime.now().date(), end_date=d_now)
        send_mail(
            'NDF',
            "Project Support",
            settings.EMAIL_ADMIN,
            [user.email],
            html_message="Congratulations!, Project support created"
        )
    else:
        project = get_object_or_404(project_support, user=user)
        d_now = project.end_date
        d_now = d_now.replace(year=d_now.year + 1)
        project.end_date = d_now
        send_mail(
            'NDF',
            "Project Support Renewed",
            settings.EMAIL_ADMIN,
            [user.email],
            html_message="Congratulations!, Project support Renewed"
        )
    project.save()

    return render(request, 'paypal/payment_done.html')


@csrf_exempt
def payment_done_donation(request):
    item = request.POST['item_name1']
    item = item.split(',')
    donating_amount = item[0]
    paid_amount = float(request.POST['mc_gross'])

    quantity = int(request.POST['quantity1'])

    user = request.user
    # charge = stripe.Charge.create(
    #     amount=amount_temp,
    #     currency='usd',
    #     description=voucher_type,
    #     source=request.POST['stripeToken']
    # )
    frequency = item[5]
    duration = item[6]
    first_name = item[1]
    last_name = item[2]
    street_address = item[7]
    postal_code = item[8]
    country = item[3]
    state = item[10]
    city = item[9]
    email = item[4]

    donate = donations.objects.create(frequency=frequency, duration=duration, donating_amount=donating_amount,
                                      paid_amount=paid_amount, first_name=first_name,
                                      last_name=last_name, street_address=street_address, postal_code=postal_code,
                                      country=country, state=state, city=city, email=email,
                                      user=user)
    donate.save()
    send_mail(
        'NDF',
        "Donation",
        settings.EMAIL_ADMIN,
        [email],
        html_message="Congratulations!, Your donation is successful."
    )

    return render(request, 'paypal/payment_done.html')


@csrf_exempt
def payment_canceled(request):
    return render(request, 'paypal/payment_cancelled.html')


def payment_canceled_membership(request):
    return render(request, 'paypal/payment_cancelled.html')


stripe.api_key = settings.STRIPE_SECRET_KEY


@csrf_exempt
def charge(request):  # new
    if request.method == 'POST':

        voucher_type = request.POST['voucher_type']
        amount_temp = float(request.POST['amount'])

        quantity = int(request.POST['quantity'])
        amount = amount_temp / quantity
        amount = amount / 100
        user = request.user
        # charge = stripe.Charge.create(
        #     amount=amount_temp,
        #     currency='usd',
        #     description=voucher_type,
        #     source=request.POST['stripeToken']
        # )
        codes = ''
        for i in range(0, quantity):
            while 1:
                code = str(uuid.uuid4().int)[:16]
                t = iter(code)
                voucher_code = "-".join(a + b + c +
                                        d for a, b, c, d in zip(t, t, t, t))
                voucher_codes = Voucher.objects.all()
                unique = True
                for vouch in voucher_codes:
                    if voucher_code == vouch.voucher_code:
                        unique = False

                if unique == True:
                    break
            v = Voucher.objects.create(voucher_code=voucher_code, voucher_type=voucher_type, amount=amount,
                                       purchase_time=datetime.now(), used_by=user)
            v.save()
            codes = codes + voucher_code + '<br>'
        send_mail('NDF', " ", settings.EMAIL_ADMIN, [request.user.email], html_message="Your NDF Voucher of type <b>" +
                  voucher_type + "</b> has been created Successfully.<br> Your voucher code is <h3>" + codes + "</h3>")
        send_mail(
            'NDF',
            " ",
            settings.EMAIL_ADMIN,
            [settings.EMAIL_ADMIN],
            html_message="An NDF Voucher of type <b>" + voucher_type + "</b> has been created by User <b>" +
            request.user.email + "</b>.<br>Voucher code is <h3>" + codes + "</h3>"
        )
        return render(request, 'paypal/charge.html')


@csrf_exempt
def charge_membership(request):  # new
    if request.method == 'POST':

        chapter = request.POST['voucher_type']
        amount_temp = float(request.POST['amount'])
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        country = request.POST['res_country']
        email = request.POST['email']
        password = request.POST['password']
        try:
            user = User.objects.create_user(
                username=first_name, email=email, password=password)
            user.save()
        except:
            msg = 'Username or email already exists'
            countries = Country.objects.all()
            groups = Professional_Group.objects.all()
            chapters = Chapter.objects.all()
            context = {
                'register_section': True,
                'countries': countries,
                'groups': groups,
                'chapters': chapters,
                'msg': msg

            }

            return render(request,
                          "register.html",
                          context
                          )
        auth.login(request, user)
        professional = request.POST['professional']

        quantity = int(request.POST['quantity'])
        amount = amount_temp / quantity
        amount = amount / 100

        # charge = stripe.Charge.create(
        #     amount=amount_temp,
        #     currency='usd',
        #     description=voucher_type,
        #     source=request.POST['stripeToken']
        # )
        d_now = date.today()
        d_now = d_now.replace(year=d_now.year + 1)
        member = membership.objects.create(chapter=chapter, first_name=first_name, last_name=last_name,
                                           country=country, email=email, professional_group=professional,
                                           user=user, start_date=datetime.now().date(), end_date=d_now)
        member.save()
        send_mail(
            'NDF',
            "Membership Registration",
            settings.EMAIL_ADMIN,
            [email],
            html_message="Congratulations!, Your are registered as a member.<br>Your professional group is: " + str(
                member.professional_group) + ", Chapter name is : " + str(
                member.chapter) + " and member ID is : " + str(member.id) + " "
        )
        return render(request, 'paypal/charge.html')


@csrf_exempt
def charge_membership_renew(request):  # new
    if request.method == 'POST':
        user = request.user
        member = membership.objects.filter(user=user).last()
        d_now = member.end_date
        d_now = d_now.replace(year=d_now.year + 1)
        member.end_date = d_now
        member.save()
        send_mail(
            'NDF',
            "Membership Renewed",
            settings.EMAIL_ADMIN,
            [user.email],
            html_message="Congratulations!, Your membership is renewed"
        )
        return render(request, 'paypal/charge.html')


@csrf_exempt
def charge_donation(request):  # new
    if request.method == 'POST':
        donating_amount = request.POST['voucher_type']
        paid_amount = float(request.POST['amount'])
        paid_amount = paid_amount / 100
        quantity = int(request.POST['quantity'])

        user = request.user
        # charge = stripe.Charge.create(
        #     amount=amount_temp,
        #     currency='usd',
        #     description=voucher_type,
        #     source=request.POST['stripeToken']
        # )
        frequency = request.POST['frequency']
        duration = request.POST['duration']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        street_address = request.POST['address']
        postal_code = request.POST['postal_code']
        country = request.POST['res_country']
        state = request.POST['state']
        city = request.POST['city']
        email = request.POST['email']

        donate = donations.objects.create(frequency=frequency, duration=duration, donating_amount=donating_amount,
                                          paid_amount=paid_amount, first_name=first_name,
                                          last_name=last_name, street_address=street_address, postal_code=postal_code,
                                          country=country, state=state, city=city, email=email,
                                          user=user)
        donate.save()
        send_mail(
            'NDF',
            "Donation",
            settings.EMAIL_ADMIN,
            [email],
            html_message="Congratulations!, Your donation is successful."
        )

        return render(request, 'paypal/charge.html')


@csrf_exempt
def charge_donationn(request):  # new
    if request.method == 'POST':
        donating_amount = request.POST['voucher_type']
        paid_amount = float(request.POST['amount'])
        paid_amount = paid_amount / 100
        quantity = int(request.POST['quantity'])

        user = request.user
        # charge = stripe.Charge.create(
        #     amount=amount_temp,
        #     currency='usd',
        #     description=voucher_type,
        #     source=request.POST['stripeToken']
        # )
        frequency = request.POST['frequency']
        duration = request.POST['duration']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        street_address = request.POST['address']
        postal_code = request.POST['postal_code']
        country = request.POST['res_country']
        state = request.POST['state']
        city = request.POST['city']
        email = request.POST['email']

        donate = donations.objects.create(frequency=frequency, duration=duration, donating_amount=donating_amount,
                                          paid_amount=paid_amount, first_name=first_name,
                                          last_name=last_name, street_address=street_address, postal_code=postal_code,
                                          country=country, state=state, city=city, email=email,
                                          user=user)
        donate.save()
        send_mail(
            'NDF',
            "Donation",
            settings.EMAIL_ADMIN,
            [email],
            html_message="Congratulations!, Your donation is successful."
        )

        return render(request, 'paypal/charges.html')


@csrf_exempt
def charge_project_support(request):  # new
    if request.method == 'POST':

        voucher_type = request.POST['voucher_type']
        amount_temp = float(request.POST['amount'])
        upgrade = request.POST['upgrade']

        quantity = int(request.POST['quantity'])
        amount = amount_temp / quantity
        amount = amount / 100
        user = request.user
        # charge = stripe.Charge.create(
        #     amount=amount_temp,
        #     currency='usd',
        #     description=voucher_type,
        #     source=request.POST['stripeToken']
        # )
        package = request.POST['package']
        user = request.user
        d_now = date.today()
        d_now = d_now.replace(year=d_now.year + 1)
        if upgrade == 'no':
            project = project_support.objects.create(package=package, paid_amount=amount_temp, user=user,
                                                     start_date=datetime.now().date(), end_date=d_now)
            send_mail(
                'NDF',
                "Project Support",
                settings.EMAIL_ADMIN,
                [user.email],
                html_message="Congratulations!, Project support created"
            )
        else:
            try:
                project = project_support.objects.get(user=user)
            except:
                context = {'donations_section': True,
                           'msg': 'There is no such Project Support.'}

                return render(request, 'dashboard/index.html', context)
            d_now = project.end_date
            d_now = d_now.replace(year=d_now.year + 1)
            project.end_date = d_now
            project.paid_amount = amount_temp
            send_mail('NDF', "Project Support Renewed", settings.EMAIL_ADMIN, [
                      user.email], html_message="Congratulations!, Project support Renewed")

    project.save()

    return render(request, 'paypal/charge.html')


def logout_User(request):
    auth.logout(request)
    return redirect('Index')
