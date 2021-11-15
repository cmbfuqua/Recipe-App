/****************************************
Tables that need to be prepopulated with static data:
- Measurements (cups, teaspoons,etc.)
- Permissions
- Role_Permissions
- Role
Tables that need to be prepopulated with test data:
- Group
- User_Group
- User
Tables that we will populate through the program
- Ingredients
- Recipe Step Ingredient
- Recipe
- Recipe Category 
- Book category
- Recipe Book
- user book
****************************************/
-- ------------Static Data Population------------------------------
use recipe_app;
-- Measurements table
insert into measurement(measurement,abbreviation)
values ('inch','in');
insert into measurement(measurement,abbreviation)
values ('ounce','oz');
insert into measurement(measurement,abbreviation)
values ('pound','lbs');
insert into measurement(measurement,abbreviation)
values ('teaspoon','tsp');
insert into measurement(measurement,abbreviation)
values ('tablespoon','tbsp');
insert into measurement(measurement,abbreviation)
values ('fluid ounce','fl oz');
insert into measurement(measurement,abbreviation)
values ('cup','c');
insert into measurement(measurement,abbreviation)
values('pint','pt');
insert into measurement(measurement,abbreviation)
values('quart','qt');
insert into measurement(measurement,abbreviation)
values('gallon','gal');
insert into measurement(measurement,abbreviation)
values ('Farenheit','F');
-- Permissions

INSERT INTO permissions (permission_name,permission_desc)
values('request to join','allows the user to request to join a group');
INSERT INTO permissions (permission_name,permission_desc)
values('remove admin','allows the group creator to remove an admin');
INSERT INTO permissions (permission_name,permission_desc)
values('add admin','allows the group creator to add an admin');
INSERT INTO permissions (permission_name,permission_desc)
values('remove member','allows a group admin to remove a member');
INSERT INTO permissions (permission_name,permission_desc)
values('add member','allows a group admin to add a member');
INSERT INTO permissions (permission_name,permission_desc)
values('delete group','allows a user to delete a group');
INSERT INTO permissions (permission_name,permission_desc)
values('edit group','allows a user to edit group details');
INSERT INTO permissions (permission_name,permission_desc)
values('create group','allows a user to create a recipe book group');
INSERT INTO permissions (permission_name,permission_desc)
values('comment','allows a user to make comments on a recipe');
INSERT INTO permissions (permission_name,permission_desc)
values('share recipe','allows a user to share a recipe they are assigned to');
INSERT INTO permissions (permission_name,permission_desc)
values('view recipe','allows a user to view a recipe they are assigned to');
INSERT INTO permissions (permission_name,permission_desc)
values('delete recipe','allows a user to delete a recipe they are assigned to');
INSERT INTO permissions (permission_name,permission_desc)
values('edit recipe','allows a user to edit a recipe they are assigned to');
INSERT INTO permissions (permission_name,permission_desc)
values('create recipe','allows the user to create a recipe');

-- Role
/*
- group level roles
group creator
admin
member
- recipe book level roles
owner
co-owner
viewer
*/
-- -----------------------recipe level
insert into roles(role_name)
values('viewer');
insert into roles(role_name)
values('co-owner');
insert into roles(role_name)
values('owner');
-- ---------------------group level
insert into roles(role_name)
values('member');
insert into roles(role_name)
values('admin');
insert into roles(role_name)
values('group creator');
-- Role_Permissions
/*
create recipe
edit recipe
delete recipe
view recipe
share recipe
comment on recipe
--------------------
create group
edit group
delete group
add members
remove members
add admin
remove admin
request to join a group
*/
-- ------------------------ recipe owner
insert into role_permission(role_id,permission_id)
values((select role_id from roles where role_name ='owner'),
	   (select permission_id from permissions where permission_name = 'create recipe'));
insert into role_permission(role_id,permission_id)
values((select role_id from roles where role_name ='owner'),
	   (select permission_id from permissions where permission_name = 'edit recipe'));










