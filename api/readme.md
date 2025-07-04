# Application informations

The endless universe codex

## Author

Boris Le Bon

## Project description

The Endless Universe Codex is a fansite dedicated to the Endless Universe from Amplitude Studio. The website provides comprehensive information about the lore and allows users to search through the vast universe's details easily.

## install and use the repo

To use this repository, you need to have Python installed. 
You can install all dependencies by running the following command in your terminal:
```
pip install -r requirement
```

Make sure the `requirements.txt` file is in the root directory of the project.

### using the backend

in the terminal go to the folder named api and type : 
```
uvicorn src.main:app --reload
```

you can use the swagger of the application clicking on the URL and typing /docs

### using the frontend

open another tab in your IDE and open the folder endlesscodex
then type :
```
yarn start
```

### Commit organization and contributions

Currently, I am the only contributor to this repository.

The naming convention for git commits follows this pattern:
`[concerned] action: comment`

`[concerned]` -> indicates the part of the project affected by the commit, such as `[backend]` or `[frontend]` (React in this case).
`action` -> describes the type of change being made, such as `add`, `fix`, or `update`.

Example: `(EC-00001)[API] feat: new API endpoint for user authentication`.








