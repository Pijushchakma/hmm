from django.conf.urls import url
from django.urls import path
from django.contrib.auth import views as auth_views

# App View Import Statements
from . import views

urlpatterns = [
    
    # Home View URL
    url(r'^$', 
        views.home, 
        name="Index"
    ),

	# Who We Are View
	path("who-we-are/", 
        views.who, 
        name="Who We Are"
    ),
    
    #History View URL
    path("history/", 
        views.history, 
        name="History"
    ),
    
    # Teams View URL
    path("teams/",
        views.teams,
        name="Teams"
    ),
    
    # Team Detail View URL
    path("team_detail/<int:id>", 
        views.team_detail, 
        name="Team Detail"
    ),
    
    # FAQs View URL
    path("faqs",
        views.faqs,
        name="FAQs"
    ),
	
	# Contact Us View URL
    path("contact",
        views.contact,
        name="Contact Us"
    ),
    
    # Projects View URL
    path("projects",
        views.projects,
        name="Projects"
    ),
    
    # Project Detail View URL
    path("project_detail/<int:id>", 
        views.project_detail, 
        name="Project Detail"
    ),
    
    # Professional Groups View URL
    path("professional_groups",
        views.professional_groups,
        name="Professional Groups"
    ),
    
    # Project Detail View URL
    path("professional_group_detail/<int:id>", 
        views.professional_detail, 
        name="Professional Group Detail"
    ),
    
    # Create Local Chapter View URL
    path("create-local-chapter",
        views.LocalChapter,
        name="Create Local Chapter"
    ),
    
    # Chapter Resources View URL
    path("chapter-resources",
        views.ChapterResources,
        name="Chapter Resources"
    ),
    
    # Find A Chapter View URL
    path("find-a-chapter",
        views.FindChapter,
        name="Find A Chapter"
    ),
    
    # Find A Chapter View URL
    path("terms-and-conditions",
        views.terms,
        name="Terms and Conditions"
    ),
    
    # News View URL
    path("News",
        views.news,
        name="News"
    ),
    
    # News Detail View URL
    path("news_detail/<int:id>", 
        views.news_detail, 
        name="News Detail"
    ),
    
    #Join NDF View URL
    path("register/", 
        views.register, 
        name="Join NDF"
    ),
    
    #Become Our Partner View URL
    path("become-our-partner/", 
        views.partner, 
        name="Become Our Partner"
    ),

    #Sign-In to NDF View URL
    path("login/", 
        views.login, 
        name="Sign-In NDF"
    ),

    #User Dashboard View URL
    path("dashboard/", 
        views.dashboard, 
        name="Dashboard"
    ),

    #Create Chapter View URL
    path("create_chapter/", 
        views.create_chapter, 
        name="Create Chapter"
    ),

    #Suggestion View URL
    path("suggestion/", 
        views.suggestion, 
        name="Suggestion"
    ),

    #Project Support View URL
    path("support/", 
        views.support, 
        name="Project Support Fee"
    ),

    #Purchase Vouchers View URL
    path("vouchers/", 
        views.vouchers, 
        name="Purchase Vouchers"
    ),

    #Donations View URL
    path("donation/", 
        views.donation, 
        name="Donations"
    ),
    
    #Donations View URL
    path("make-donation/", 
        views.donate, 
        name="Make Donations"
    ),

    #Profile View URL
    path("profile/", 
        views.profile, 
        name="Profile"
    ),

    #Change Password View URL
    path("change_password/", 
        views.change_password, 
        name="change_password"
    ),

    #Invite Friends View URL
    path("invite_friends/", 
        views.invite_friends, 
        name="Invite Friends"
    ),

    # User Logout View URL
    url(r'^logout/$', 
        views.logout_User, 
        name= "logout_user_url"
    ),

    #Load States View URL
    path('ajax/load-states/', 
        views.load_states, 
        name='ajax_load_states'
    ),
    
    #Load Cities View URL
    path('ajax/load-cities/', 
        views.load_cities, 
        name='ajax_load_cities'
    ),

    #Load Chapters View URL
    path('ajax/load-chapter/', 
        views.load_chapter, 
        name='ajax_load_chapter'
    ),
    path('process-payment/', views.process_payment, name='process_payment'),
    path('process-payment-membership/', views.process_payment_membership, name='process_payment_membership'),
    path('payment-done/', views.payment_done, name='payment_done'),
    path('payment-done-membership/', views.payment_done_membership, name='payment_done_membership'),
    path('payment-done-membership-renew/', views.payment_done_membership_renew, name='payment_done_membership_renew'),
    path('payment-done-donation/', views.payment_done_project_support, name='payment_done_project_support'),
    path('payment-done-project-support/', views.payment_done_donation, name='payment_done_donation'),
    path('payment-cancelled/', views.payment_canceled, name='payment_cancelled'),
    path('payment-cancelled-membership/', views.payment_canceled_membership, name='payment_cancelled_membership'),
    path('charge/', views.charge, name='charge'),
    path('charge-membership/', views.charge_membership, name='charge_membership'),
    path('charge-membership-renew/', views.charge_membership_renew, name='charge_membership_renew'),
    path('charge-donation/', views.charge_donation, name='charge_donation'),
    path('charge-donationn/', views.charge_donationn, name='charge_donationn'),
    path('charge-project-support/', views.charge_project_support, name='charge_project_support'),
    path('endorse-member/', views.endorse_member, name='endorse_member'),
    # Password Reset urls
    path('reset_password/',
         auth_views.PasswordResetView.as_view(
             template_name="dashboard/password_reset.html"),
         name="reset_password"),

    path('reset_password_sent/',
         auth_views.PasswordResetDoneView.as_view(
             template_name="dashboard/password_reset_sent.html"),
         name="password_reset_done"),

    path('reset/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(
             template_name="dashboard/password_reset_form.html"),
         name="password_reset_confirm"),

    path('reset_password_complete/',
         auth_views.PasswordResetCompleteView.as_view(
             template_name="dashboard/password_reset_done.html"),
         name="password_reset_complete"),
]