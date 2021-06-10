# advertyzement-backend-task

An API server made as part of selection task at Advertyzement.

You can try out by going to this [link](https://advertyzement-backend-task.herokuapp.com/gql).

Data used in the database can be found in [this repo](https://github.com/Amanskywalker/indian_banks).

## Local Setup

Clone the repo to your machine.

### Setting Up Virtual Environment

* To create a virtual environment, run \
`python3 -m venv env`
* To install all dependencies, run \
`pip install -r requirements.txt`

### Setting Up the Database

* Ensure postgresql is installed. 
* Download the dump file from [here](https://github.com/Amanskywalker/indian_banks).
* Using the sql dump file, restore the dump using \
`psql <database_name> < <file_name>` \
Replace <database_name> with the name of the database to which it is being restored to and replace <file_name> with the name of the dump file.

### Creating Environment Variables

* Create a file called .env \
`touch .env`
* Add the following content to .env file. \
`DATABASE_URL=<replace with database url>` \
The database url would be of the format \
`dialect+driver://username:password@host:port/database`

### Running the Program

* To run, in the terminal, run \
`python app.py`

