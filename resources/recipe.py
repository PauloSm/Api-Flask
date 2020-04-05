from flask import request
from flask_restful import Resource 
from http import HTTPStatus

from models.recipe import recipe_list, Recipe 

class RecipeResourceList(Resource):

	def get(self):

		recipes_public = []

		for recipe in recipe_list:
			if recipe.is_publish:
				recipes_public.append(recipe.data)

		return {'data': recipes_public}

	def post(self):

		data = request.get_json()
		recipe = Recipe(data['name'], data['description'], 
			data['num_of_servings'], data['cook_time'], data['directions'])

		recipe_list.append(recipe)
		return {'data': recipe.data}, HTTPStatus.CREATED

class RecipeResource(Resource):
	
	def get(self, recipe_id):
		
		recipe = next((recipe for recipe in recipe_list if recipe.id == 
			recipe_id), None)

		if recipe is None:
			return {'message': 'recipe not found'}, HTTPStatus.NOT_FOUND

		return {'data': recipe.data}

	def put(self, recipe_id):

		recipe = next((recipe for recipe in recipe_list if recipe.id == 
			recipe_id), None)

		if recipe is None:
			return {'message': 'recipe not found'}, HTTPStatus.NOT_FOUND

		data = request.get_json()

		recipe.name = data['name']
		recipe.description = data['description']
		recipe.cook_time = data['cook_time']
		recipe.num_of_servings = data['num_of_servings']
		recipe.directions = data['directions']

		return {}, HTTPStatus.OK

	def delete(self, recipe_id):

		recipe = next((recipe for recipe in recipe_list if recipe.id == 
			recipe_id), None)

		if recipe is None:
			return {'message': 'recipe not found'}, HTTPStatus.NOT_FOUND

		recipe_list.remove(recipe)
		return {}, HTTPStatus.NO_CONTENT

class RecipeResourcePublish(Resource):

	def put(self, recipe_id):
		recipe = next((recipe for recipe in recipe_list if recipe.id == 
			recipe_id), None)

		if recipe is None:
			return {'message': 'recipe not found'}, HTTPStatus.NOT_FOUND

		recipe.is_publish = True

		return {}, HTTPStatus.NO_CONTENT

	def delete(self, recipe_id):
		recipe = next((recipe for recipe in recipe_list if recipe.id == 
			recipe_id), None)

		if recipe is None:
			return {'message': 'recipe not found'}, HTTPStatus.NOT_FOUND

		recipe.is_publish = False
		return {}, HTTPStatus.NO_CONTENT