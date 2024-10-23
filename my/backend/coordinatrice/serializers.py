# admin_custom/serializers.py
from rest_framework import serializers
from admin_custom.models import  Utilisateur, MaitreApprentissage, Apprenti, TuteurPedagogique, CoordinatriceApprentissage, Enseignant


class MaitreApprentissageSerializer(serializers.ModelSerializer):
    class Meta:                                                                                                                                   
        model = MaitreApprentissage
        fields = ['telephone']

    def update(self, instance, validated_data):
        instance.telephone = validated_data.get('telephone', instance.telephone)
        #instance.entreprise = validated_data.get('entreprise', instance.entreprise)
        #instance.date_naissance = validated_data.get('date_naissance',instance.date_naissance)
        instance.save()
        return instance

class TutoratSerializer(serializers.ModelSerializer):
    class Meta:
        model = TuteurPedagogique
        fields = ['telephone','date_naissance']

    def update(self, instance, validated_data):
        instance.telephone = validated_data.get('telephone', instance.telephone)
        instance.date_naissance = validated_data.get('date_naissance',instance.date_naissance)
        instance.save()
        return instance
    
class ApprentiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Apprenti
        fields = ['tuteur_pedagogique', 'maitre_apprentissage']
        # il y'a encore une reflexion à faire
    def update(self, instance, validated_data):
        instance.tuteur_pedagogique = validated_data.get('tuteur_pedagogique', instance.tuteur_pedagogique)
        instance.maitre_apprentissage = validated_data.get('maitre_apprentissage', instance.maitre_apprentissage)
        instance.save()
        return instance
