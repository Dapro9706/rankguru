Quickstart
=============

Retrieving Auth
----------------

This Rankguru wrapper relies on the Rankguru Auth which can be accessed by a browser with the following steps

**Step 1:** Open rankguru in a browser and make sure you are logged in

**Step 2:** Open developer tools in browser (Ctrl+Shift+I)

**Step 3:** Click on Console and paste the following code snippet

.. code-block:: javascript 

   const ca=document.cookie.split(";");for(let o=0;o<ca.length;o++){let n=ca[o];for(;" "===n.charAt(0);)n=n.substring(1);0===n.indexOf("token=")&&(t=n.substring("token=".length,n.length),console.log({Accept:"application/json, text/plain, */*",Authorization:t,accesscontroltoken:localStorage.accessControlToken}))}

This will give a JSON object and then you can copy the object this is now your current auth which will change every time you log out

**Step 4:** Now to test it you can make a `header.json` file and paste in the object, then make a test python script and paste in the following snippet

.. code-block:: python

   from rankguru.utils import verify_header
   import json

   with open('header.json') as f:
      print('Your header validity is ' + verify_header(json.load(f)))

You should get the following output if your header is valid

.. code-block:: c

    Your header validity is True


