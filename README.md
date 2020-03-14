# DJANGO REST FRAMWORK APPLICATION

## With Generic API Views and Mixins:
## Generic class based views
## Permissions
## Pagination

### One of the key benefits of using the Generic Views in Django as in Django
One of the key benefits of using the Generic Views in Django as in Django
REST Framework, is that these offer us a large amount of ready-to-use code
that is useful in most of the most common development scenarios.
CRUD operations in a model-backed API for example will be implemented in
the same way in most cases: reinventing the wheel every time would be a
waste of time!
DRF has a class called GenericAPIView that extends the APIView class already
seen in previous lessons, adding to this some very useful methods and
attributes.

The GenericAPIView class is often used with Mixins, classes that provide
further functionalities to our views increasing their capabilities.
It is important to note that as we will see, the Mixin Classes provide action
methods such as .list() or .create() rather than defining the handler methods,
such as .get() or .post() directly, as we did using the APIView class.
