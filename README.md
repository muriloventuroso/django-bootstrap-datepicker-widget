# django-bootstrap-datepicker

This package is **compatible with both Bootstrap 3 and 4**, by giving the option to use a FontAwesome icon rather than a Glyphicon.

This package is intended to be used with [bootstrap-datepicker](https://github.com/uxsolutions/bootstrap-datepicker) and has been tested with v1.7.1.

This project was originally a fork of [nkunihiko/django-bootstrap3-datetimepicker](https://github.com/nkunihiko/django-bootstrap3-datetimepicker) and hence similar to [qoobic/django-bootstrap3-datepicker](https://github.com/qoobic/django-bootstrap3-datepicker), 
but it now has the following breaking changes:

* js/css files are no longer included in the project, managing them is up to the user, eg. using 
[grablib](https://github.com/samuelcolvin/grablib).
* the widget no longer has js/css assets. these are left for you to deploy as you wish.
* bug/warning fixes
* remove support for python 2.6 and associated clean up

## Install
1. Run `pip install django-bootstrap-datepicker-widget`
2. Add `bootstrap_datepicker` to your `INSTALLED_APPS`

## Example

#### forms.py

```python
from bootstrap_datepicker.widgets import DatePicker
from django import forms

  class ToDoForm(forms.Form):
      todo = forms.CharField(
          widget=forms.TextInput(attrs={"class": "form-control"}))
      date = forms.DateField(
          widget=DatePicker(options={"format": "YYYY-MM-DD"}, fontawesome=True))
```

The `options` will be passed to the JavaScript datetimepicker instance. 
Available `options` are explained in the [bootstrap-datepicker docs](https://bootstrap-datepicker.readthedocs.io/en/stable/options.html)

You don't need to set the `language` option, 
because it will be set the current language of the thread automatically.

#### template.html

```html
<!DOCTYPE html>
<html>
  <head>
    <!-- load all required js/css yourself here -->
  </head>
  <body>
    <form method="post" role="form">
      {{ form|bootstrap }}
      {% csrf_token %}
      <div class="form-group">
        <input type="submit" value="Submit" class="btn btn-primary" />
      </div>
    </form>
  </body>
</html>
```

Here we assume you're using [django-bootstrap-form](https://github.com/tzangms/django-bootstrap-form) or 
[django-jinja-bootstrap-form](https://github.com/samuelcolvin/django-jinja-bootstrap-form) but you can
draw out your HTML manually.

## Requirements

* Python >= 2.7
* Django >= 1.8
* Bootstrap >= 3
* FontAwesome >= 1.0 if using Bootstrap 4+
* Moment >= 2.10.6
* bootstrap-datepicker >= 1.7.1
