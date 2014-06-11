
## Description

The Registration App is used to register user with the clearing House [Ohouse](https://github.com/motine/Ohouse). It implements the registration server API i.e., "register_user". The registration client, 
sends user's information such as: 
- First Name 
- Last Name 
- User Name 
- Email 

Furthermore, the registration app provides the user with an option to either let the app generate SSH keys for him / her, or let the users provide the key to the client themselves. 


## Dependencies

The registration app has some package dependencies, Python dependencies can then be installed using: pip install -r requirements.txt.  


## Configuration 

To Configure the Registration App, follow these steps: 
- cp registation_app_config.json.example registation_app_config.json 
- Open registation_app_config.json and configure it with the registration server IP and Port defined [here](https://github.com/motine/Ohouse)

Example: 

{{gist}}: https://gist.github.com/zanetworker/ee4fedbeab782d797d0b 

## Run 

To run the registration app, run "python  registration_client.py" 
