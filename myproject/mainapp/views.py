from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    return HttpResponse('''<h1>Welcome to my First Django Project!!!🥳
                        <h1>''')

def contact(request):
    return HttpResponse('''
                        <h1>Contact Page</h1>
                        <ul>
                            <li>Name: Mithilesh Das</li>
                            <li>DOB: 21-03-2006</li>
                            <li>Dept: CSE</li>
                        </ul>
                        ''')