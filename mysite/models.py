from django.db import models
from django.db import connections
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from ckeditor_uploader.fields import RichTextUploadingField
from smart_selects.db_fields import ChainedForeignKey
from cities_light.models import City, Country, Region, SubRegion
from django_countries.fields import CountryField
from django.utils.translation import ugettext_lazy as _
from django.contrib import admin
from simple_history.models import HistoricalRecords
from django.utils.timezone import now
# Create your models here.


COUNTRY_CHOICES = (
    ('AF', 'AFGHANISTAN'),
    ('AL', 'ALBANIA'),
    ('DZ', 'ALGERIA'),
    ('AS', 'AMERICAN SAMOA'),
    ('AD', 'ANDORRA'),
    ('AO', 'ANGOLA'),
    ('AI', 'ANGUILLA'),
    ('AQ', 'ANTARCTICA'),
    ('AG', 'ANTIGUA AND BARBUDA'),
    ('AR', 'ARGENTINA'),
    ('AM', 'ARMENIA'),
    ('AW', 'ARUBA'),
    ('AU', 'AUSTRALIA'),
    ('AT', 'AUSTRIA'),
    ('AZ', 'AZERBAIJAN'),
    ('BS', 'BAHAMAS'),
    ('BH', 'BAHRAIN'),
    ('BD', 'BANGLADESH'),
    ('BB', 'BARBADOS'),
    ('BY', 'BELARUS'),
    ('BE', 'BELGIUM'),
    ('BZ', 'BELIZE'),
    ('BJ', 'BENIN'),
    ('BM', 'BERMUDA'),
    ('BT', 'BHUTAN'),
    ('BO', 'BOLIVIA'),
    ('BA', 'BOSNIA AND HERZEGOVINA'),
    ('BW', 'BOTSWANA'),
    ('BV', 'BOUVET ISLAND'),
    ('BR', 'BRAZIL'),
    ('IO', 'BRITISH INDIAN OCEAN TERRITORY'),
    ('BN', 'BRUNEI DARUSSALAM'),
    ('BG', 'BULGARIA'),
    ('BF', 'BURKINA FASO'),
    ('BI', 'BURUNDI'),
    ('KH', 'CAMBODIA'),
    ('CM', 'CAMEROON'),
    ('CA', 'CANADA'),
    ('CV', 'CAPE VERDE'),
    ('KY', 'CAYMAN ISLANDS'),
    ('CF', 'CENTRAL AFRICAN REPUBLIC'),
    ('TD', 'CHAD'),
    ('CL', 'CHILE'),
    ('CN', 'CHINA'),
    ('CX', 'CHRISTMAS ISLAND'),
    ('CC', 'COCOS (KEELING) ISLANDS'),
    ('CO', 'COLOMBIA'),
    ('KM', 'COMOROS'),
    ('CG', 'CONGO'),
    ('CD', 'CONGO, THE DEMOCRATIC REPUBLIC OF'),
    ('CK', 'COOK ISLANDS'),
    ('CR', 'COSTA RICA'),
    ('CI', "CÃ”TE D'IVOIRE"),
    ('HR', 'CROATIA'),
    ('CU', 'CUBA'),
    ('CY', 'CYPRUS'),
    ('CZ', 'CZECH REPUBLIC'),
    ('DK', 'DENMARK'),
    ('DJ', 'DJIBOUTI'),
    ('DM', 'DOMINICA'),
    ('DO', 'DOMINICAN REPUBLIC'),
    ('EC', 'ECUADOR'),
    ('EG', 'EGYPT'),
    ('SV', 'EL SALVADOR'),
    ('GQ', 'EQUATORIAL GUINEA'),
    ('ER', 'ERITREA'),
    ('EE', 'ESTONIA'),
    ('ET', 'ETHIOPIA'),
    ('FK', 'FALKLAND ISLANDS (MALVINAS)'),
    ('FO', 'FAROE ISLANDS'),
    ('FJ', 'FIJI'),
    ('FI', 'FINLAND'),
    ('FR', 'FRANCE'),
    ('GF', 'FRENCH GUIANA'),
    ('PF', 'FRENCH POLYNESIA'),
    ('TF', 'FRENCH SOUTHERN TERRITORIES'),
    ('GA', 'GABON'),
    ('GM', 'GAMBIA'),
    ('GE', 'GEORGIA'),
    ('DE', 'GERMANY'),
    ('GH', 'GHANA'),
    ('GI', 'GIBRALTAR'),
    ('GR', 'GREECE'),
    ('GL', 'GREENLAND'),
    ('GD', 'GRENADA'),
    ('GP', 'GUADELOUPE'),
    ('GU', 'GUAM'),
    ('GT', 'GUATEMALA'),
    ('GN', 'GUINEA'),
    ('GW', 'GUINEA'),
    ('GY', 'GUYANA'),
    ('HT', 'HAITI'),
    ('HM', 'HEARD ISLAND AND MCDONALD ISLANDS'),
    ('HN', 'HONDURAS'),
    ('HK', 'HONG KONG'),
    ('HU', 'HUNGARY'),
    ('IS', 'ICELAND'),
    ('IN', 'INDIA'),
    ('ID', 'INDONESIA'),
    ('IR', 'IRAN, ISLAMIC REPUBLIC OF'),
    ('IQ', 'IRAQ'),
    ('IE', 'IRELAND'),
    ('IL', 'ISRAEL'),
    ('IT', 'ITALY'),
    ('JM', 'JAMAICA'),
    ('JP', 'JAPAN'),
    ('JO', 'JORDAN'),
    ('KZ', 'KAZAKHSTAN'),
    ('KE', 'KENYA'),
    ('KI', 'KIRIBATI'),
    ('KP', "KOREA, DEMOCRATIC PEOPLE'S REPUBLIC OF"),
    ('KR', 'KOREA, REPUBLIC OF'),
    ('KW', 'KUWAIT'),
    ('KG', 'KYRGYZSTAN'),
    ('LA', "LAO PEOPLE'S DEMOCRATIC REPUBLIC"),
    ('LV', 'LATVIA'),
    ('LB', 'LEBANON'),
    ('LS', 'LESOTHO'),
    ('LR', 'LIBERIA'),
    ('LY', 'LIBYAN ARAB JAMAHIRIYA'),
    ('LI', 'LIECHTENSTEIN'),
    ('LT', 'LITHUANIA'),
    ('LU', 'LUXEMBOURG'),
    ('MO', 'MACAO'),
    ('MK', 'MACEDONIA, THE FORMER YUGOSLAV REPUBLIC OF'),
    ('MG', 'MADAGASCAR'),
    ('MW', 'MALAWI'),
    ('MY', 'MALAYSIA'),
    ('MV', 'MALDIVES'),
    ('ML', 'MALI'),
    ('MT', 'MALTA'),
    ('MH', 'MARSHALL ISLANDS'),
    ('MQ', 'MARTINIQUE'),
    ('MR', 'MAURITANIA'),
    ('MU', 'MAURITIUS'),
    ('YT', 'MAYOTTE'),
    ('MX', 'MEXICO'),
    ('FM', 'MICRONESIA, FEDERATED STATES OF'),
    ('MD', 'MOLDOVA, REPUBLIC OF'),
    ('MC', 'MONACO'),
    ('MN', 'MONGOLIA'),
    ('MS', 'MONTSERRAT'),
    ('MA', 'MOROCCO'),
    ('MZ', 'MOZAMBIQUE'),
    ('MM', 'MYANMAR'),
    ('NA', 'NAMIBIA'),
    ('NR', 'NAURU'),
    ('NP', 'NEPAL'),
    ('NL', 'NETHERLANDS'),
    ('AN', 'NETHERLANDS ANTILLES'),
    ('NC', 'NEW CALEDONIA'),
    ('NZ', 'NEW ZEALAND'),
    ('NI', 'NICARAGUA'),
    ('NE', 'NIGER'),
    ('NG', 'NIGERIA'),
    ('NU', 'NIUE'),
    ('NF', 'NORFOLK ISLAND'),
    ('MP', 'NORTHERN MARIANA ISLANDS'),
    ('NO', 'NORWAY'),
    ('OM', 'OMAN'),
    ('PK', 'PAKISTAN'),
    ('PW', 'PALAU'),
    ('PS', 'PALESTINIAN TERRITORY, OCCUPIED'),
    ('PA', 'PANAMA'),
    ('PG', 'PAPUA NEW GUINEA'),
    ('PY', 'PARAGUAY'),
    ('PE', 'PERU'),
    ('PH', 'PHILIPPINES'),
    ('PN', 'PITCAIRN'),
    ('PL', 'POLAND'),
    ('PT', 'PORTUGAL'),
    ('PR', 'PUERTO RICO'),
    ('QA', 'QATAR'),
    ('RE', 'RÃ‰UNION'),
    ('RO', 'ROMANIA'),
    ('RU', 'RUSSIAN FEDERATION'),
    ('RW', 'RWANDA'),
    ('SH', 'SAINT HELENA'),
    ('KN', 'SAINT KITTS AND NEVIS'),
    ('LC', 'SAINT LUCIA'),
    ('PM', 'SAINT PIERRE AND MIQUELON'),
    ('VC', 'SAINT VINCENT AND THE GRENADINES'),
    ('WS', 'SAMOA'),
    ('SM', 'SAN MARINO'),
    ('ST', 'SAO TOME AND PRINCIPE'),
    ('SA', 'SAUDI ARABIA'),
    ('SN', 'SENEGAL'),
    ('CS', 'SERBIA AND MONTENEGRO'),
    ('SC', 'SEYCHELLES'),
    ('SL', 'SIERRA LEONE'),
    ('SG', 'SINGAPORE'),
    ('SK', 'SLOVAKIA'),
    ('SI', 'SLOVENIA'),
    ('SB', 'SOLOMON ISLANDS'),
    ('SO', 'SOMALIA'),
    ('ZA', 'SOUTH AFRICA'),
    ('GS', 'SOUTH GEORGIA AND SOUTH SANDWICH ISLANDS'),
    ('ES', 'SPAIN'),
    ('LK', 'SRI LANKA'),
    ('SD', 'SUDAN'),
    ('SR', 'SURINAME'),
    ('SJ', 'SVALBARD AND JAN MAYEN'),
    ('SZ', 'SWAZILAND'),
    ('SE', 'SWEDEN'),
    ('CH', 'SWITZERLAND'),
    ('SY', 'SYRIAN ARAB REPUBLIC'),
    ('TW', 'TAIWAN, PROVINCE OF CHINA'),
    ('TJ', 'TAJIKISTAN'),
    ('TZ', 'TANZANIA, UNITED REPUBLIC OF'),
    ('TH', 'THAILAND'),
    ('TL', 'TIMOR'),
    ('TG', 'TOGO'),
    ('TK', 'TOKELAU'),
    ('TO', 'TONGA'),
    ('TT', 'TRINIDAD AND TOBAGO'),
    ('TN', 'TUNISIA'),
    ('TR', 'TURKEY'),
    ('TM', 'TURKMENISTAN'),
    ('TC', 'TURKS AND CAICOS ISLANDS'),
    ('TV', 'TUVALU'),
    ('UG', 'UGANDA'),
    ('UA', 'UKRAINE'),
    ('AE', 'UNITED ARAB EMIRATES'),
    ('GB', 'UNITED KINGDOM'),
    ('US', 'UNITED STATES'),
    ('UM', 'UNITED STATES MINOR OUTLYING ISLANDS'),
    ('UY', 'URUGUAY'),
    ('UZ', 'UZBEKISTAN'),
    ('VU', 'VANUATU'),
    ('VN', 'VIET NAM'),
    ('VG', 'VIRGIN ISLANDS, BRITISH'),
    ('VI', 'VIRGIN ISLANDS, U.S.'),
    ('WF', 'WALLIS AND FUTUNA'),
    ('EH', 'WESTERN SAHARA'),
    ('YE', 'YEMEN'),
    ('ZW', 'ZIMBABWE')
)

PREFIX_CHOICES = (
    ('Mr', 'Mr'),
    ('Mrs', 'Mrs'),
    ('Miss', 'Miss'),
    ('Dr.', 'Dr.'),
    ('Prof.', 'Prof.'),
    ('Chief', 'Chief'),
    ('Hon', 'Hon'),
    ('Alhaji', 'Alhaji'),
    ('Alhaja', 'Alhaja')
)

VOUCHER_CHOICES = (
    ('CountryVoucher', 'CountryVoucher'),
    ('GeneralVoucher', 'GeneralVoucher')
)
VOUCHER_STATUS_CHOICES = (
    ('Okay', 'Okay'),
    ('Used', 'Used')
)


class Country_Voucher_Price(models.Model):
    country = models.ForeignKey(Country,on_delete=models.CASCADE)
    price = models.FloatField()

    def __str__(self):
        return self.country.name


class General_Voucher_Price(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True)
    price = models.FloatField()

    def __str__(self):
        return self.name


class Slider(models.Model):
    title = models.CharField(max_length=100)
    sub_title = models.CharField(max_length=100, default='Join us Today')
    img = models.ImageField(upload_to='slider_img')
    desc = RichTextUploadingField()
    left_Button_Name = models.CharField(max_length=100, default='Learn more')
    left_Button_Link = models.URLField(default='https://www.ndf.ng')
    right_Button_Name = models.CharField(max_length=100, default='Join Now')
    right_Button_Link = models.URLField(default='https://ndf.ng')

    

class Projects(models.Model):
    title = models.CharField(max_length=100)
    img = models.ImageField(upload_to='projects')
    desc = RichTextUploadingField()

class Team(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    img = models.ImageField(upload_to='teams')
    designation = models.CharField(max_length=100)
    fb = models.URLField(default="https://facebook.com")
    tw = models.URLField(default="https://twitter.com")
    go = models.URLField(default="https://google.com")
    bio = RichTextUploadingField()

class New(models.Model):
    title = models.CharField(max_length=100)
    img = models.ImageField(upload_to='news')
    desc = RichTextUploadingField()
    upload_date = models.DateField(auto_now=True)


class FAQ(models.Model):
    question = models.CharField(max_length=1000)
    answer = RichTextUploadingField()
    approve = models.NullBooleanField(blank=True, default=None, null=True)

class Professional_Group(models.Model):
    name = models.CharField(max_length=100)
    objective = RichTextUploadingField()
    desc = RichTextUploadingField()
    img = models.ImageField(upload_to='professional')
    project = models.CharField(max_length=100, blank=True)
    chairman = models.CharField(max_length=100, blank=True)
    vice_chairman = models.CharField(max_length=100, blank=True)
    secretary = models.CharField(max_length=100, blank=True)

    class Meta:
        verbose_name_plural = _("Professional Groups")


class Chapter(models.Model):
    country = models.CharField(max_length=100, choices=COUNTRY_CHOICES)
    name = models.CharField(max_length=100)
    fee = models.DecimalField(decimal_places=2, max_digits=5)





class Voucher(models.Model):
    voucher_code = models.CharField(max_length=50,null=True)
    voucher_type = models.CharField(max_length=20, choices=VOUCHER_CHOICES, null=True, blank=True)
    amount = models.DecimalField(decimal_places=2, max_digits=5, null=True, blank=True)
    status = models.CharField(max_length=10, choices=VOUCHER_STATUS_CHOICES,default="Okay")
    purchase_time = models.DateTimeField(null=True, blank=True)
    used_time = models.DateTimeField(null=True, blank=True)
    used_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    
    def __str__(self):
        return self.voucher_code

class Voucher_uses(models.Model):
    Voucher_obj = models.ForeignKey(Voucher,on_delete=models.CASCADE)
    used_by = models.ForeignKey(User,on_delete=models.CASCADE)
    used_to = models.EmailField(blank=True,null=True)
    time = models.TimeField(auto_now=True, blank=True)
    date = models.DateField(auto_now=True, blank=True)
    timestamp = models.DateTimeField(default=now)

    def __str__(self):
        return self.Voucher_obj.voucher_code

# class Country(models.Model):
#     name = models.CharField(max_length=30)

#     def __str__(self):
#         return self.name

# class State(models.Model):
#     country = models.ForeignKey(Country, on_delete=models.CASCADE)
#     name = models.CharField(max_length=30)

#     def __str__(self):
#         return self.name

# class City(models.Model):
#     state = models.ForeignKey(State, on_delete=models.CASCADE)
#     name = models.CharField(max_length=30)

#     def __str__(self):
#         return self.name


class Create_Chapter(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete= models.CASCADE)
    name = models.CharField(max_length=100)
    address = models.TextField()
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    state = ChainedForeignKey(
        Region,
        chained_field="country",
        chained_model_field="country_id",
        show_all=False,
        auto_choose=True
    )
    city = ChainedForeignKey(
        SubRegion, 
        chained_field="state",
        chained_model_field="region_id",
        show_all=False,
        auto_choose=True
    )
    zip_code = models.CharField(max_length=100)
    estimated_membership = models.CharField(max_length=10)
    president = models.CharField(max_length=100, blank=True, null=True)
    secretary = models.CharField(max_length=100, blank=True, null=True)
    membership_officer = models.CharField(max_length=100, blank=True, null=True)
    treasurer = models.CharField(max_length=100, blank=True, null=True)
    program_officer = models.CharField(max_length=100, blank=True, null=True)
    vice_president = models.CharField(max_length=100, blank=True, null=True)
    legal_officer = models.CharField(max_length=100, blank=True, null=True)
    welfare_officer = models.CharField(max_length=100, blank=True, null=True)
    aggreeTerms = models.BooleanField(blank=True, default=True)
    approve = models.NullBooleanField(blank=True, default=None, null=True)

    class Meta:
        verbose_name_plural = _("Local Chapters")



class Suggestion(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete= models.CASCADE)
    title = models.CharField(max_length=100)
    message = RichTextUploadingField()

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.TextField(max_length=20)
    message = RichTextUploadingField()
    
# class showCountries(models.Model):
#     country = models.CharField(max_length=100)
#     class meta:
#         db_table = 

class UserProfileManager(models.Manager):
         pass

class UserProfile(models.Model):
    #user = models.OneToOneField(User)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address1 = models.CharField(max_length=500, default='')
    address2 = models.CharField(max_length=500, default='')
    postal_code = models.CharField(max_length=20, default='')
    country = models.ForeignKey(Country, on_delete=models.CASCADE) 
    state = ChainedForeignKey(
        Region,
        chained_field="country",
        chained_model_field="country_id",
        show_all=False,
        auto_choose=True
    )
    city = ChainedForeignKey(
        SubRegion, 
        chained_field="state",
        chained_model_field="region_id",
        show_all=False,
        auto_choose=True
    )
    dob = models.DateField(auto_now=False, default='')
    phoneNumber = models.IntegerField(default=0)
    professionalGroup = models.ForeignKey(Professional_Group, on_delete=models.CASCADE)
    profession = models.CharField(max_length=100)
    image = models.ImageField(upload_to='profile_image' , blank=True)


    def __str__(self):
        return self.user.username


class UserProfile_new(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100,blank=True)
    last_name = models.CharField(max_length=100,blank=True)
    street_address = models.CharField(max_length=100,blank=True)
    street_address_optional = models.CharField(max_length=100,blank=True)
    postal_code =  models.CharField(max_length=100,blank=True)
    country = models.CharField(max_length=100,blank=True)
    state = models.CharField(max_length=100,blank=True)
    city = models.CharField(max_length=100,blank=True)
    email = models.EmailField(blank=True)
    phone = models.IntegerField(default=00)
    dob = models.DateField(auto_now=False,blank=True)
    profession = models.CharField(max_length=100,blank=True)
    image = models.ImageField(upload_to='profile_image' , blank=True)
    history = HistoricalRecords()

    def __str__(self):
        return self.user.username








def createProfile(sender, **kwargs):
    if kwargs['created']:
        user_profile = UserProfile.objects.created(user=kwargs['instance'])
        
        post_save.connect(createProfile, sender=User)


class membership(models.Model):
    chapter = models.CharField(max_length=50)
    first_name = models.CharField(max_length=20,null=True,blank=True)
    last_name = models.CharField(max_length=20,null=True,blank=True)
    country = models.CharField(max_length=50,null=True,blank=True)
    email = models.EmailField(null=True,blank=True)
    professional_group = models.CharField(max_length=100,null=True,blank=True)
    start_date = models.DateField(null=True,blank=True)
    end_date = models.DateField(null=True, blank=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)


    def __str__(self):
        return self.chapter


class project_support(models.Model):
    package = models.CharField(max_length=20)
    payment_type = models.CharField(max_length=20,null=True,blank=True)
    amount = models.CharField(max_length=10,null=True,blank=True)
    paid_amount = models.CharField(max_length=10,null=True,blank=True)
    start_date = models.DateField(null=True,blank=True)
    end_date = models.DateField(null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.package


class donations(models.Model):
    donating_amount = models.CharField(max_length=10)
    frequency = models.CharField(max_length=50)
    paid_amount = models.CharField(max_length=10,null=True,blank=True)
    duration = models.CharField(max_length=50,null=True,blank=True)
    dedicate = models.BooleanField(null=True,blank=True)
    first_name = models.CharField(max_length=20, null=True, blank=True)
    last_name = models.CharField(max_length=20, null=True, blank=True)
    street_address = models.CharField(max_length=100, null=True, blank=True)
    postal_code = models.CharField(max_length=10, null=True, blank=True)
    country = models.CharField(max_length=50, null=True, blank=True)
    state = models.CharField(max_length=50, null=True, blank=True)
    city = models.CharField(max_length=50, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.donating_amount


class endorsement(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    endorsed_by = models.ForeignKey(User,on_delete=models.CASCADE, related_name='endorsed_by', null=True, blank=True)


