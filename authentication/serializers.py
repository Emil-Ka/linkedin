from rest_framework import serializers
from authentication.models import User
from authentication.groups import groups_dict

#create - валидирует данные на register: берет пароль из данных, создает юзера со всеми данными 
# кроме пароля, задает ему active, если пароль есть, то добавляем его, но захэшированный, сохраняет юзера

class UserSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = ['id', 'email', 'first_name', 'last_name', 'photo', 'bio', 'is_active', 'password', 'role']
    extra_kwargs = {
      'password': {
        'write_only': True
      }
    }

  def create(self, validated_data):
    print('valid', validated_data)
    print('type', type(validated_data))
    password = validated_data.pop('password', None)
    role = validated_data.get('role')
    instance = self.Meta.model(**validated_data)
    instance.is_active = True

    if password is not None:
      instance.set_password(password)

    instance.save()

    instance.groups.add(groups_dict[int(role)])

    return instance

  # def validate(self, data):
  #   if (data['role'] is not None) and not (data['role'] == 'USER' or data['role'] == 'HR'):
  #     raise serializers.ValidationError({'error': 'role is invalid'})

  #   return data