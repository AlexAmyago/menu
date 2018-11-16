# Simple Menu

## The motivation
Provides one of the many variants for serving restaurant menu through Rest Api.

- Each menu restaurant/cafe contains menu items
- Menu Items can has list of modifiers (Side item, Topping, Sauce)
- At the same time each modifier can possibly has own modifier/modifiers 


## Technical choice

### Stack
As a basis the next packages has been chosen:
- `Django Framework` (Flask and Falcon also was considered but Django is most suitable for fast developing without extra efforts)
- `Django Rest Framework (DRF)` (well known solution for providing REST api with great flexibility)
- `Django Nested Routes(DNR)` (extension for `DRF` to provide workaround for nested resources)  

### Challenge
Technically, the task is more about how to keep hierarchical data.
There is a great [article](http://mikehillyer.com/articles/managing-hierarchical-data-in-mysql/) about subject 
 
For solving such specific task two packages has been considered:
- `DJANGO-MPTT`
- `DJANGO-TREEBEARD`

After reviewing [packages above](https://djangopackages.org/grids/g/trees-and-graphs/) 
I stopped at `DJANGO-MPTT` (great documentation, support, positive reviews)

## Response examples

Spots:
```
GET /restaurants/
[
    {
        "id": 1,
        "name": "Hide",
        "details": "Some beautiful place with decent wine.",
        "location": "London"
    }
]
```

Dishes
```
GET /restaurants/1/dish/

[
    {
        "id": 2,
        "name": "List Aperol Spritz",
        "details": "Champagne, blood orange puree, soda, rocks",
        "dish_modifiers": [
            {
                "id": 2,
                "name": "Strawberry Ice cream",
                "details": "",
                "extra": []
            }
        ],
        "category": [
            {
                "id": 1,
                "name": "FEATURED DISHES"
            }
        ]
    },
    {
        "id": 1,
        "name": "Grilled Pheasant",
        "details": "Idaho pheasant marinated and grilled. Sautéed greens, spicy butter gnocchi",
        "cost": "10"
        "dish_modifiers": [
            {
                "id": 1,
                "name": "Garlic Souce",
                "details": "",
                "extra": [
                    {
                        "id": 2,
                        "parent": 1,
                        "name": "Strawberry Ice cream",
                        "details": ""
                    }
                ]
            }
        ],
        "category": [
            {
                "id": 1,
                "name": "FEATURED DISHES"
            }
        ]
    }
]
```

### How to test
- Clone repo
- Create DB
- Provide ENV vars with DB data
    ```ENV=local
    DB_USER=postgres
    DB_PASS=postgres
    DB_HOST=db
    DB_NAME=postgres
    DB_PORT=5432
    ```

- Under venv install requirements (`pip3 install -r requirements.txt`)
- Run develop server `python3 manage.py runserver localhost:8000`
- As an alternative for local you can setup docker by following the next [link](https://docs.docker.com/compose/django/#define-the-project-components)


### Final Words
It is just an example of solution.
What can be added:
- versioning (to avoid shooting to the leg in future)
- tests (I've not provided it, because solution is based on `DRF` which already covered with tests)
