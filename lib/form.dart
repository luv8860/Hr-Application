import 'package:flutter/material.dart';
import 'package:hr_application/custombox.dart';
import 'dart:ui' show ImageFilter;

import 'package:hr_application/custombox_result.dart';

class FormPage extends StatefulWidget {
  @override
  _FormPageState createState() => _FormPageState();
}

class _FormPageState extends State<FormPage> {
  String department;
  String region;
  String education;
  String gender;
  String recruitment;
  String kpi;
  String award;
  String age;
  String trainings;
  String service;
  String avg;
  String rate;

  final _formKey = GlobalKey<FormState>();

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: Container(
          decoration: BoxDecoration(
            gradient: LinearGradient(
                begin: Alignment.topLeft,
                end: Alignment.bottomRight,
                colors: [
                  Color.fromRGBO(17, 113, 213, 1),
                  Color.fromRGBO(249, 248, 113, 1)
                ]),
          ),
          child: Form(
            key: _formKey,
            child: Column(children: [
              SizedBox(
                height: 30.0,
              ),
              Padding(
                padding: const EdgeInsets.all(5.0),
                child: Row(
                  children: [
                    SizedBox(
                      width: 15.0,
                    ),
                    Text('HR Application',
                        style: TextStyle(
                            fontFamily: 'Source Sans Pro',
                            fontWeight: FontWeight.w700,
                            color: Colors.white,
                            fontSize: 40)),
                    SizedBox(
                      width: 25.0,
                    ),
                    IconButton(
                      icon: Icon(
                        Icons.info,
                        color: Colors.white,
                      ),
                      iconSize: 30,
                      onPressed: () {
                        showGeneralDialog(
                          barrierDismissible: true,
                          barrierLabel: '',
                          barrierColor: Colors.black38,
                          transitionDuration: Duration(milliseconds: 100),
                          pageBuilder: (ctx, anim1, anim2) => CustomDialogBox(
                              title: "How to use This App",
                              descriptions:
                                  "Fill in all the details accurately and Press the Check the data button So that our Machine learning model can accurately detect whether to provide promotion to the candidate.",
                              text: "OK"),
                          transitionBuilder: (ctx, anim1, anim2, child) =>
                              BackdropFilter(
                            filter: ImageFilter.blur(
                                sigmaX: 4 * anim1.value,
                                sigmaY: 4 * anim1.value),
                            child: FadeTransition(
                              child: child,
                              opacity: anim1,
                            ),
                          ),
                          context: context,
                        );
                      },
                    )
                  ],
                ),
              ),
              SizedBox(
                height: 30.0,
              ),
              Expanded(
                child: SingleChildScrollView(
                  physics: BouncingScrollPhysics(),
                  child: Column(
                    mainAxisAlignment: MainAxisAlignment.spaceBetween,
                    crossAxisAlignment: CrossAxisAlignment.center,
                    children: [
                      SizedBox(
                        height: 15.0,
                      ),
                      Container(
                          width: 300,
                          child: ButtonTheme(
                            buttonColor: Colors.white,
                            alignedDropdown: true,
                            child: DropdownButton<String>(
                              value: department,
                              isExpanded: true,
                              hint: Text(
                                "Select Department",
                                style: TextStyle(color: Colors.white),
                              ),
                              items: <String>[
                                'Finance',
                                'HR',
                                'Legal',
                                'Operations',
                                'Procurement',
                                'R&D',
                                'Sales & Marketing',
                                'Technology',
                                'Analytics'
                              ].map((String value) {
                                return new DropdownMenuItem<String>(
                                  value: value,
                                  child: new Text(value),
                                );
                              }).toList(),
                              onChanged: (value) {
                                department = value;
                                setState(() {
                                  print(department);
                                });
                              },
                            ),
                          )),
                      SizedBox(
                        height: 15.0,
                      ),
                      Container(
                          width: 300,
                          child: ButtonTheme(
                            buttonColor: Colors.white,
                            alignedDropdown: true,
                            child: DropdownButton<String>(
                              value: region,
                              isExpanded: true,
                              hint: Text(
                                "Select Region",
                                style: TextStyle(color: Colors.white),
                              ),
                              items: <String>[
                                'region_1',
                                'region_2',
                                'region_3',
                                'region_4',
                                'region_5',
                                'region_6',
                                'region_7',
                                'region_8',
                                'region_9',
                                'region_10',
                                'region_11',
                                'region_12',
                                'region_13',
                                'region_14',
                                'region_15',
                                'region_16',
                                'region_17',
                                'region_18',
                                'region_19',
                                'region_20',
                                'region_21',
                                'region_22',
                                'region_23',
                                'region_24',
                                'region_25',
                                'region_26',
                                'region_27',
                                'region_28',
                                'region_29',
                                'region_30',
                                'region_31',
                                'region_32',
                                'region_33',
                                'region_34'
                              ].map((String value) {
                                return new DropdownMenuItem<String>(
                                  value: value,
                                  child: new Text(value),
                                );
                              }).toList(),
                              onChanged: (value) {
                                region = value;
                                setState(() {
                                  print(region);
                                });
                              },
                            ),
                          )),
                      SizedBox(
                        height: 15.0,
                      ),
                      Container(
                          width: 300,
                          child: ButtonTheme(
                            buttonColor: Colors.white,
                            alignedDropdown: true,
                            child: DropdownButton<String>(
                              value: education,
                              isExpanded: true,
                              hint: Text(
                                "Select Education",
                                style: TextStyle(color: Colors.white),
                              ),
                              items: <String>[
                                'Master\'s & above',
                                'Bachelor\'s',
                                'Below Secondary'
                              ].map((String value) {
                                return new DropdownMenuItem<String>(
                                  value: value,
                                  child: new Text(value),
                                );
                              }).toList(),
                              onChanged: (value) {
                                education = value;
                                setState(() {
                                  print(education);
                                });
                              },
                            ),
                          )),
                      SizedBox(
                        height: 15.0,
                      ),
                      Container(
                          width: 300,
                          child: ButtonTheme(
                            buttonColor: Colors.white,
                            alignedDropdown: true,
                            child: DropdownButton<String>(
                              value: rate,
                              isExpanded: true,
                              hint: Text(
                                "Select Previous Year rating",
                                style: TextStyle(color: Colors.white),
                              ),
                              items: <String>['0', '1', '2', '3', '4', '5']
                                  .map((String value) {
                                return new DropdownMenuItem<String>(
                                  value: value,
                                  child: new Text(value),
                                );
                              }).toList(),
                              onChanged: (value) {
                                rate = value;
                                setState(() {
                                  print(rate);
                                });
                              },
                            ),
                          )),
                      SizedBox(
                        height: 15.0,
                      ),
                      Container(
                          width: 300,
                          child: ButtonTheme(
                            buttonColor: Colors.white,
                            alignedDropdown: true,
                            child: DropdownButton<String>(
                              value: gender,
                              isExpanded: true,
                              hint: Text(
                                "Select Gender",
                                style: TextStyle(color: Colors.white),
                              ),
                              items: <String>['male', 'female']
                                  .map((String value) {
                                return new DropdownMenuItem<String>(
                                  value: value,
                                  child: new Text(value),
                                );
                              }).toList(),
                              onChanged: (value) {
                                gender = value;
                                setState(() {
                                  print(gender);
                                });
                              },
                            ),
                          )),
                      SizedBox(
                        height: 15.0,
                      ),
                      Container(
                          width: 300,
                          child: ButtonTheme(
                            buttonColor: Colors.white,
                            alignedDropdown: true,
                            child: DropdownButton<String>(
                              value: recruitment,
                              isExpanded: true,
                              hint: Text(
                                "Select Recruitment Channel",
                                style: TextStyle(color: Colors.white),
                              ),
                              items: <String>['sourcing', 'referred', 'other']
                                  .map((String value) {
                                return new DropdownMenuItem<String>(
                                  value: value,
                                  child: new Text(value),
                                );
                              }).toList(),
                              onChanged: (value) {
                                recruitment = value;
                                setState(() {
                                  print(recruitment);
                                });
                              },
                            ),
                          )),
                      SizedBox(
                        height: 15.0,
                      ),
                      Container(
                          width: 300,
                          child: ButtonTheme(
                            buttonColor: Colors.black,
                            alignedDropdown: true,
                            child: DropdownButton<String>(
                              value: kpi,
                              isExpanded: true,
                              hint: Text("KPI >80",
                                  style: TextStyle(color: Colors.white)),
                              items: <String>['Yes', 'No'].map((String value) {
                                return new DropdownMenuItem<String>(
                                  value: value,
                                  child: new Text(value),
                                );
                              }).toList(),
                              onChanged: (value) {
                                kpi = value;
                                setState(() {
                                  print(kpi);
                                });
                              },
                            ),
                          )),
                      SizedBox(
                        height: 15.0,
                      ),
                      Container(
                          width: 300,
                          child: ButtonTheme(
                            buttonColor: Colors.black,
                            alignedDropdown: true,
                            child: DropdownButton<String>(
                              value: award,
                              isExpanded: true,
                              hint: Text("Award Recieved?",
                                  style: TextStyle(color: Colors.white)),
                              items: <String>['Yes', 'No'].map((String value) {
                                return new DropdownMenuItem<String>(
                                  value: value,
                                  child: new Text(value),
                                );
                              }).toList(),
                              onChanged: (value) {
                                award = value;
                                setState(() {
                                  print(award);
                                });
                              },
                            ),
                          )),
                      SizedBox(
                        height: 15.0,
                      ),
                      Container(
                          width: 300,
                          child: TextFormField(
                              onChanged: (value) {
                                age = value;
                              },
                              decoration: InputDecoration(
                                hintText: '    Enter The Age',
                                hintStyle: TextStyle(color: Colors.white),
                              ))),
                      SizedBox(
                        height: 15.0,
                      ),
                      Container(
                          width: 300,
                          child: TextFormField(
                              onChanged: (value) {
                                trainings = value;
                              },
                              decoration: InputDecoration(
                                hintText:
                                    '    Enter The No. of trainings attended',
                                hintStyle: TextStyle(color: Colors.white),
                              ))),
                      SizedBox(
                        height: 15.0,
                      ),
                      Container(
                          width: 300,
                          child: TextFormField(
                              onChanged: (value) {
                                service = value;
                              },
                              decoration: InputDecoration(
                                hintText: '    Enter The Length of service',
                                hintStyle: TextStyle(color: Colors.white),
                              ))),
                      SizedBox(
                        height: 15.0,
                      ),
                      Container(
                          width: 300,
                          child: TextFormField(
                              onChanged: (value) {
                                avg = value;
                              },
                              decoration: InputDecoration(
                                hintText: 'Enter The Average Training Score',
                                hintStyle: TextStyle(color: Colors.white),
                              ))),
                      SizedBox(
                        height: 30.0,
                      ),
                      Container(
                        height: 50,
                        margin: EdgeInsets.symmetric(horizontal: 50),
                        decoration: BoxDecoration(
                            borderRadius: BorderRadius.circular(50),
                            color: Color.fromRGBO(17, 113, 213, 1)),
                        child: Center(
                          child: ButtonTheme(
                              minWidth: 200.0,
                              child: FlatButton(
                                  onPressed: () {
                                    showGeneralDialog(
                                      barrierDismissible: true,
                                      barrierLabel: '',
                                      barrierColor: Colors.black38,
                                      transitionDuration:
                                          Duration(milliseconds: 100),
                                      pageBuilder: (ctx, anim1, anim2) =>
                                          CustomDialogBox2(
                                        department: department,
                                        recruitment: recruitment,
                                        region: region,
                                        rate: rate,
                                        education: education,
                                        kpi: kpi,
                                        award: award,
                                        trainings: trainings,
                                        service: service,
                                        avg: avg,
                                      ),
                                      transitionBuilder:
                                          (ctx, anim1, anim2, child) =>
                                              BackdropFilter(
                                        filter: ImageFilter.blur(
                                            sigmaX: 4 * anim1.value,
                                            sigmaY: 4 * anim1.value),
                                        child: FadeTransition(
                                          child: child,
                                          opacity: anim1,
                                        ),
                                      ),
                                      context: context,
                                    );
                                  },
                                  child: Text(
                                    "Check The Data",
                                    style: TextStyle(
                                        color: Colors.white,
                                        fontWeight: FontWeight.bold),
                                  ))),
                        ),
                      ),
                      SizedBox(
                        height: 30.0,
                      ),
                    ],
                  ),
                ),
              ),
            ]),
          )),
    );
  }
}
