Quickstart
=============

Retrieving Auth
----------------

This Rankguru wrapper relies on the Rankguru Auth which can be accessed by 2 methods

**__1) Browser__**

**Step 1:** Open rankguru in a browser and make sure you are logged in

**Step 2:** Open developer tools in browser (Ctrl+Shift+I)

**Step 3:** Click on Console and paste the following code snippet

.. code-block:: javascript 

   const ca=document.cookie.split(";");for(let o=0;o<ca.length;o++){let n=ca[o];for(;" "===n.charAt(0);)n=n.substring(1);0===n.indexOf("token=")&&(t=n.substring("token=".length,n.length),console.log({Accept:"application/json, text/plain, */*",Authorization:t,accesscontroltoken:localStorage.accessControlToken}))}

This will give a JSON object and then you can copy the object this is now your current auth which will change every time you log out

**Step 4:** Now to test it you can make a `header.json` file and paste in the object, then make a test python script and paste in the following snippet

.. code-block:: python

   from rankguru.request_handler import verify_header
   import json

   with open('header.json') as f:
      print('Your header validity is ' + verify_header(json.load(f)))

You should get the following output if your header is valid

.. code-block:: c

    Your header validity is True


**__2) Code__**

This is way easier to use but it logs you out of rankguru in your main pc or app everytime you use

.. code block::python

   from rankguru.utils import get_header
   from rankguru.request_handler import verify_header

   h = get_header (your scs id, your scs password)
   print('Your header validity is ' + verify_header(h))

   #ps. its recommended to store header in .json file and running this only in the event of an AuthError

Retrieving Tests
----------------

Now you have a valid auth.
Go to rankguru.com go to tests and select a category.

The url will be in the form 

https://www.rankguru.com/test/online-test-list?textBookCode=[id]&&textBookName=name

id -> is the text book id and yor can use it to retrieve tests

.. code-block::

   from rankguru import RG
   import json

   with open('header.json') as f:
      h=json.load(f)
   
   api = RG(h)

   id= #id you got from url

   print(api.get_tests(id))

   # ps. If there are many tests with the same name this might not be correct


Retrieving Answers
------------------

Now from the previous step copy qpid of the necessary test and the run the following snippet

.. code-block::

   from rankguru import RG
   import json

   with open('header.json') as f:
      h=json.load(f)
   
   api = RG(h)

   qpid= #qpid you got from previous step

   print(api.get_ans(qpid))