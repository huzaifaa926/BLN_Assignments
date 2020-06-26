// I hereby confirm that I have not cheated or copied in this assignment. I have obtain help from following resources:
//1- https://medium.com/coinmonks/solidity-tutorial-returning-structs-from-public-functions-e78e48efb378
//2- https://solidity.readthedocs.io/en/v0.4.24/types.html


pragma solidity ^0.4.24;

contract student_record
{
    struct Student
    {
        uint32 id;
        string name;
        uint32 sem_no;
        uint32 sgpa;
    }
    mapping(uint32 => Student) student;
    function add_student(uint32 _id, string n) public
    {
        student[_id].id = _id;
        student[_id].name = n;
    }
    function add_semester_record(uint32 sem, uint32 gpa, uint32 _id) public
    {
        student[_id].sem_no = sem;
        student[_id].sgpa = gpa;
    }
    function update_student(uint32 sem, uint32 gpa, uint32 _id) public
    {
        student[_id].sem_no = sem;
        student[_id].sgpa = gpa;
    }
    function retrieve_student(uint32 id) public view returns(string, uint32, uint32, uint32)
    {
        return (student[id].name, student[id].id, student[id].sem_no, student[id].sgpa);
    }
}
