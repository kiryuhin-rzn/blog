from django.test import TestCase
from app_news.models import News, File
from django.urls import reverse
from django.test import Client
from django.contrib.auth.models import User
from app_news.forms import MultiFileForm, NewsForm, UploadNewsForm
from app_users.forms import ExtendedRegisterForm
from django.core.files.uploadedfile import SimpleUploadedFile
import io
from io import BytesIO
import csv

class TestRegisterAuthentication(TestCase):
    def test_register_post(self):
        c = Client()
        form_data = {'username': 'Juliana',  'password1': 'johnpassword42AS21/*', 'password2': 'johnpassword42AS21/*'}
        c.post('/users/register/', form_data)
        u = User.objects.get(username__exact='Juliana')
        u.set_password('johnpassword42AS21/*')
        c.login(username='Juliana', password=u.set_password(u.password))
        response = c.get('/users/login/', follow=True)
        #print(response.context)
        response = c.get(reverse('news_list'))
        print(str(response.context['user']))
        #self.assertEqual(str(response.context['user']), 'Juliana')

    def test_authentication_post(self):
        c = Client()
        User.objects.create_user('Juliana', "juliana@dev.io", 'johnpassword42AS21/*')
        form_data = {'username': 'Juliana',  'password': 'johnpassword42AS21/*'}
        c.post('/users/login/', form_data)
        response = c.get(reverse('news_list'))
        self.assertEqual(str(response.context['user']), 'Juliana')
        #print(str(response.context['user']))
        #self.assertEqual(str(response.context['user']), 'Juliana')
        #print(response.context)

    def test_authentication_unsuccessfully(self):
        c = Client()
        User.objects.create_user('Juliana', "juliana@dev.io", 'johnpassword42AS21/*')
        form_data = {'username': 'Juliana',  'password': ' '}
        c.post('/users/login/', form_data)
        response = c.get(reverse('news_list'))
        #print(str(response.context['user']))
        self.assertNotEqual(str(response.context['user']), 'Juliana')


    def test_redirect_authentication(self):
        c = Client()
        User.objects.create_user('Juliana', "juliana@dev.io", 'johnpassword42AS21/*')
        form_data = {'username': 'Juliana',  'password': 'johnpassword42AS21/*'}
        response=c.post('/users/login/', form_data)
        self.assertRedirects(response, '/', status_code=302,
        target_status_code=200, fetch_redirect_response=True)

    def test_redirect_registration(self):
        c = Client()
        form_data = {'username': 'Juliana',  'password1': 'johnpassword42AS21/*', 'password2': 'johnpassword42AS21/*'}
        response=c.post('/users/register/', form_data)
        self.assertRedirects(response, '/', status_code=302,
        target_status_code=200, fetch_redirect_response=True)


class TestDownloadFile(TestCase):
    def test_post_file_image(self):
        c = Client()
        User.objects.create_superuser("admin", "juliana@dev.io", "admin")
        c.login(username='admin', password='admin')
        form_data = {'title': 'Name news', 'text':'Something news'}
        form = NewsForm(data=form_data)
        self.assertTrue(form.is_valid())
        news = form.save()
        response = c.get(reverse('news_detail', args=(str(news.id),)))
        #print(response.context['object'])
        self.assertIn(str(response.context['object']), 'Name news')
        #c.get(reverse('news_detail', args=(str(news.id),)))
        form_data_f = {'file_field': SimpleUploadedFile("file.jpg", b"file_content", content_type="image/jpg")}
        c.post('/news/1/upload_files/', form_data_f)
        response = c.get('/news/1')
        #print(response.content)
        #print(File.objects.all())


    def test_post_file_csv(self):
        c = Client()
        User.objects.create_superuser("admin", "juliana@dev.io", "admin")
        c.login(username='admin', password='admin')
        file_content = 'Buchungstag; Valuta\nBuchungstext; Auftraggeber'.encode("utf-8")
        form_data = {'file': SimpleUploadedFile('test.csv', file_content, content_type='text/csv')}
        c.post('/news/uploads/', form_data)
        response = c.get('/')
        self.assertIn('Buchungstag', str(response.context['object_list']))



        #b = io.BytesIO(b"file_content")
        #b.name = 'myimage.csv'
        #input = io.StringIO('This goes into the read buffer; This goes into the read buffer;)
        #print(input.read())
        #filename="somefilename.csv"
        '''content_type='text/csv'
        csv_data = (
        ('First row', 'Foo', 'Bar'),
        ('Second row', 'A', 'B'),
    )'''
        #video = SimpleUploadedFile("file.csv", b'This goes into the read buffer; This goes into the read buffer;', content_type='text/csv')
        #f = open("file.csv",'w')
        #f.write('hi there\n''hi there\n') #Give your csv text here.
        ## Python will convert \n to os.linesep
        #f.close()
        #self.client.post('/news/uploads/', {'video': video})
        #valid_file = 'Buchungstag;Valuta \n Buchungstext; Auftraggeber'.encode("utf-8")
        #form_data = {'file_field': SimpleUploadedFile('test.csv', valid_file, content_type='text/csv')}#content=('What?; Whay? \n That; Start \n').encode('utf-8')
        '''f = SimpleUploadedFile.from_dict(
         dict(
             filename='test.csv', content_type='text/csv',
             content=(
                 'What?; Whay? \n That; Start \n').encode(encoding='UTF-8')
         ))'''
        #c.post('/news/uploads/', {'file_field': form_data}) #dict(csvfile=f)
        #with input as fp:
            #c.post('/news/uploads/', {'name': 'files.csv', 'file_field': fp})
        #output = io.StringIO()
        #output.write('First line.\n')
        #output.getvalue()
        #with open('test_file.csv', 'rb') as fp:
        #form = UploadNewsForm(data=f)
        #print(form.errors)
        #response = c.get('/')
        #print(response.context)
        #print(File.objects.all())
        #print(File.objects.get(pk=1))












