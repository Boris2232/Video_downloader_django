# Video_downloader_django
My project on Django framework.


Hello, here i uploaded some code with description. This project helps to download videos from YouTube after inserting link.

This READMI file will introduce you to registration and login processes.


Part 1: !!! Registration Form !!!


-Desctiption:

1)"Regform" (Download_videos) folder in this project contains templates of registration form, login form and page, which confirms the registration process. Registration form collects information user's information (using html forms and views.py functions), sends it to the project's database(sqlite) and saves it. As son as fields of username and password are filled and submit button is pressed, Django redirects user to next page - Login Form.

-- Structure of regform folder -- :
1) __init__.py (unused in my project)
2) admin.py (registers model People(username + password) in django admin)
3) apps.py (opportunity to customize configuration)
4) models.py ( !!!saves username and password as a object's attribute!!! --- name = models.CharField(max_length=25, blank=False)
                password = models.CharField(max_length=15, blank=False)
   !! Returns username if the object is called)
5) test.py (test cases can be written here)
   
7) views.py (Combines views functions of three aplications)
                                  def index_1(request):
   
                                  # catches information from form
   
                                  if request.method == 'POST':
   
                                  # creates variables of login and password
   
                                    login = request.POST['username']
                                    password = request.POST['password']
   
                                    # creates object with login and password attributes
   
                                    new_user = People(name=login, password=password)
                                    #saves this field in global database
                                    new_user.save()
   
                                    # redirects to a next page (can be modified)
   
                                    return redirect("login/")
   
                                    # loads page with html + css template
   
                                  return render(request, 'index.html')

   
!!! Checking for the mistakes or incorrect username and password structure is not included here to simplify the testing activities, but this structure provides possibility to tune that.

9) templates folder (html templates of login, registration page and main page (congratulations)
10) migrations folder (data base is stored as sqlite file, possible to edit)
11) static folder (Images and css files for thet app, registration page has unique author's design)


!!!! IMPORTANT: this and other pages have design, which is made in figma and it is responsible for all types of devices (with using % or vw instead of pixels. Design changes accordingly to a resolution of a screen)


!!! Login form !!!


Description: 
Login page is designed to catch information from the input fields after clicking submit button. It has almost the same functionality as the registration form, but instead of writing new info to database, is retrieves provided username from the database (if it exists) and compares corresponding password to provided password)

Structure: 
1) views.py is located in regform folder.
2) views.py functionality:
def login_page(request):

    // Extract information of all users from database
    all_people = People.objects.all()
   
    s1 = []
       # store login and passwords in array "s1"
    for i in all_people:
        s1.append([i.name, i.password])
       # catches form
    if request.method == 'POST':
       # extract username and login from request 
        given_login = request.POST.get('username')
        given_pass = request.POST.get('password')
        # redirected = False
        for i in range(len(s1)):
       # if the login exists and corresponding password matches with provided, redirect to main page
            if s1[i][0] == given_login and s1[i][1] == given_pass:
                return HttpResponseRedirect('/congrat')
    return render(request, 'login.html')


!!! Main page !!!

Description:
Main page illustartes gif video (green tick) if the login was successfull. There is a big button to move to a next page - Video Downloader.

!!!! REMARK: Registration and login process is not fully used in this application. I decided to create this to familiarise with django functioanality, investigate the database editing process and to learn how to conduct redirects. !!!!
