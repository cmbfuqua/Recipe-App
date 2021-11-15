drop database recipe_app;
create database recipe_app;
use recipe_app;

create table measurement(
measurement_id int        NOT NULL AUTO_INCREMENT,
measurement varchar(25)   NOT NULL,
abbreviation varchar(10)  NOT NULL,
constraint pk_measurement_id primary key (measurement_id)
);

create table ingredients(
ingredient_id int           NOT NULL AUTO_INCREMENT,
ingredient_name varchar(70) NOT NULL,
measurement_id int          NOT NULL,
constraint pk_ingredient_id primary key (ingredient_id),
constraint fk_measurement_id foreign key(measurement_id) references measurement(measurement_id)
);

create table recipe_category(
category_id      int           NOT NULL AUTO_INCREMENT,
category_name    varchar(50)   NOT NULL,
constraint pk_category_id primary key (category_id)
);

create table recipe(
recipe_id            int            NOT NULL AUTO_INCREMENT,
recipe_name          varchar(50)    NOT NULL,
recipe_description   varchar(50)    NOT NULL,
category_id          int            NOT NULL,
constraint pk_recipe_id primary key (recipe_id),
constraint fk_rcategory_id foreign key (category_id) references recipe_category(category_id)
);

create table recipe_step_ingredient(
ingredient_id    int   NOT NULL,
recipe_id        int   NOT NULL,
step_description varchar(999) NOT NULL,
constraint pk_composite_ri primary key (ingredient_id,recipe_id),
constraint fk_ingredient_id foreign key (ingredient_id) references ingredients(ingredient_id),
constraint fk_recipe_id foreign key (recipe_id) references recipe(recipe_id)
);

create table recipe_book(
book_id            int       NOT NULL AUTO_INCREMENT,
book_name          int       NOT NULL,
constraint pk_book_id primary key (book_id)
);

create table book_category(
book_id        int    NOT NULL,
category_id    int    NOT NULL,
constraint pk_composite_bc primary key (book_id,category_id),
constraint fk_book_id foreign key (book_id) references recipe_book(book_id),
constraint fk_bcategory_id foreign key (category_id) references recipe_category(category_id)
);

create table recipe_group(
group_id       int           NOT NULL AUTO_INCREMENT,
group_name     varchar(100)  NOT NULL,
creation_date  date          NOT NULL,
constraint pk_group_id primary key(group_id)
);

create table users(
user_id      int            NOT NULL AUTO_INCREMENT,
fname        varchar(100)   NOT NULL,
mname        varchar(5)     NOT NULL,
lname        varchar(100)   NOT NULL,
registered   date           NOT NULL,
last_paid    date           NOT NULL,
constraint pk_user_id primary key(user_id)
);

create table user_group(
user_id     int    NOT NULL,
group_id    int    NOT NULL,
constraint pk_composite_ug primary key(user_id,group_id),
constraint fk_user_id_ug foreign key (user_id) references users(user_id),
constraint fk_group_id foreign key (group_id) references recipe_group(group_id)
);

create table permissions (
permission_id     int          NOT NULL AUTO_INCREMENT,
permission_name   varchar(25)  NOT NULL,
permission_desc   varchar(150) NOT NULL,
constraint pk_permission_id primary key (permission_id)
);

create table roles (
role_id       int             NOT NULL AUTO_INCREMENT,
role_name     varchar(50)     NOT NULL,
constraint pk_role_id primary key (role_id)
);

create table role_permission(
role_id        int     NOT NULL,
permission_id  int     NOT NULL,
constraint pk_composite_rp primary key (role_id, permission_id),
constraint fk_role_id_rp foreign key (role_id) references roles(role_id),
constraint fk_permission_id foreign key (permission_id) references permissions(permission_id)
);

create table user_book(
role_id     int     NOT NULL,
user_id     int     NOT NULL,
book_id     int     NOT NULL,
constraint pk_composite_rub primary key (role_id,user_id,book_id),
constraint fk_role_id_ub foreign key (role_id) references roles(role_id),
constraint fk_user_id_ub foreign key (user_id) references users(user_id),
constraint fk_book_id_ub foreign key (book_id) references recipe_book(book_id)
);








