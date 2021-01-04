<?xml version="1.0" encoding="UTF-8"?>
<model ref="r:29371b5e-dc1c-4afd-8293-0e94b09d5be9(Animals.sandbox)">
  <persistence version="9" />
  <languages>
    <use id="ee886be0-abf5-408e-8219-419e0e49cb3c" name="Animals" version="0" />
    <use id="f3061a53-9226-4cc5-a443-f952ceaf5816" name="jetbrains.mps.baseLanguage" version="11" />
    <use id="f2801650-65d5-424e-bb1b-463a8781b786" name="jetbrains.mps.baseLanguage.javadoc" version="2" />
  </languages>
  <imports>
    <import index="wyt6" ref="6354ebe7-c22a-4a0f-ac54-50b52ab9b065/java:java.lang(JDK/)" />
    <import index="33ny" ref="6354ebe7-c22a-4a0f-ac54-50b52ab9b065/java:java.util(JDK/)" />
  </imports>
  <registry>
    <language id="ee886be0-abf5-408e-8219-419e0e49cb3c" name="Animals">
      <concept id="5662060582600315613" name="Animals.structure.Canvas" flags="ng" index="2kcrN4">
        <child id="5662060582600315616" name="animals" index="2kcrNT" />
      </concept>
      <concept id="5662060582600315601" name="Animals.structure.Dog" flags="ng" index="2kcrN8">
        <property id="5662060582600315602" name="name" index="2kcrNb" />
        <property id="5662060582600315604" name="weight" index="2kcrNd" />
      </concept>
    </language>
    <language id="ceab5195-25ea-4f22-9b92-103b95ca8c0c" name="jetbrains.mps.lang.core">
      <concept id="1169194658468" name="jetbrains.mps.lang.core.structure.INamedConcept" flags="ng" index="TrEIO">
        <property id="1169194664001" name="name" index="TrG5h" />
      </concept>
    </language>
  </registry>
  <node concept="2kcrN4" id="4UjFxBqCHrP">
    <property role="TrG5h" value="MyAnimals" />
    <node concept="2kcrN8" id="4UjFxBqCHrQ" role="2kcrNT">
      <property role="2kcrNb" value="Rufus" />
      <property role="2kcrNd" value="50" />
    </node>
    <node concept="2kcrN8" id="4UjFxBqCHrV" role="2kcrNT">
      <property role="2kcrNb" value="Lily" />
      <property role="2kcrNd" value="40" />
    </node>
  </node>
</model>

