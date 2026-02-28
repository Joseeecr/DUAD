function gradeAvg(student){
  let gradeAvg = 0;

  for (const element of student.grades){
    gradeAvg += element.grade / student.grades.length;
  }

  return gradeAvg;
}


function highestGrade(student){
  let highest = 0;
  let highestGradeName = "";

  for (const currentElement of student.grades){
    if(currentElement.grade > highest){
      highest = currentElement.grade;
      highestGradeName = currentElement.name;
    }
  }

  return highestGradeName;
}


function lowestGrade(student){
  let lowest = Infinity;
  let lowestGradeName = "";

  for (const currentElement of student.grades){
    if(currentElement.grade < lowest){
      lowest = currentElement.grade;
      lowestGradeName = currentElement.name;
    }
  }

  return lowestGradeName;
}


function studentInformation(student){
  const gradeAvgResult = gradeAvg(student)
  const highestGradeName = highestGrade(student)
  const lowestGradeName = lowestGrade(student)

  const studentResult = {
    name: student.name,
    gradeAvg: gradeAvgResult,
    highestGrade: highestGradeName,
    lowestGrade: lowestGradeName
  };

  return studentResult;
}


const student = {
	name: "John Doe",
	grades: [
		{name: "math",grade: 80},
		{name: "science",grade: 100},
		{name: "history",grade: 60},
		{name: "PE",grade: 90},
		{name: "music",grade: 98}
	]
};

const result = studentInformation(student);

console.log(result)