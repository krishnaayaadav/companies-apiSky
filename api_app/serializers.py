from rest_framework import serializers
from .models import Company,Types
      
class CompanySerializer(serializers.Serializer):
   # fields
   pk        = serializers.IntegerField(required=False)
   comp_name = serializers.CharField(max_length=255)
   comp_type = serializers.CharField()
   comp_headq= serializers.CharField(max_length=255)
   how_old= serializers.CharField(max_length=255)
   comp_no_emp = serializers.CharField(max_length=255)
   comp_review = serializers.CharField(max_length=255)
   open_jobs   = serializers.CharField(max_length=255)
   comp_services = serializers.CharField(max_length=255)
   comp_desc     = serializers.CharField()
   
   def validate(self, attrs):
      """Validating company type here """
      typ = attrs.get('comp_type',None)
      
      if self.context['patch']:
         if not typ:
            return attrs
         else:
            try:
               comp_typ = Types.objects.get(name=typ)
            except:
               raise serializers.ValidationError('Invalid Company type')
            else:
               attrs['comp_type'] = comp_typ
               return attrs
         
      if not type:
         raise serializers.ValidationError('Company type is required')
      else:
         try:
            comp_typ = Types.objects.get(name=typ)
         except:
            raise serializers.ValidationError('Invalid Company type')
         else:
            attrs['comp_type'] = comp_typ
            return attrs
            
   def create(self, validated_data):
      """Create method to allow insertion"""
      return Company.objects.create(**validated_data)
   
   def update(self, instance, validated_data):
      instance.comp_name = validated_data.get('comp_name', instance.comp_name)
      instance.comp_type = validated_data.get('comp_type', instance.comp_type)
      instance.comp_headq = validated_data.get('comp_headq', instance.comp_headq)
      instance.how_old = validated_data.get('how_old', instance.how_old)
      instance.comp_no_emp = validated_data.get('comp_no_emp', instance.comp_no_emp)
      instance.comp_review = validated_data.get('comp_review', instance.comp_review)
      instance.open_jobs = validated_data.get('open_jobs', instance.open_jobs)
      instance.comp_services = validated_data.get('comp_services', instance.comp_services)
      instance.comp_desc = validated_data.get('comp_desc', instance.comp_desc)
      
      instance.save()
      return instance
      