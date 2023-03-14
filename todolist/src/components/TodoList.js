import todoData from "./TodoListData.json";
import {useState} from "react";
import './TodoList.css'
function TodoList(){
   const [taskList,setTaskList]=useState(todoData);
   const [statusList,setStatusList]=useState(["active","deactive"]);
   const [status,setStatus]=useState("");
   const [taskTitle,setTaskTitle]=useState("");
   
   var today = new Date(),
   time = today.getHours() + ':' + today.getMinutes() + ':' + today.getSeconds();
   const [currentTime,setCurrentTime]=useState(time);
   var today = new Date(),

   date = today.getFullYear() + '-' + (today.getMonth() + 1) + '-' + today.getDate();
   const [currentDate,setCurrentDate]=useState(date);
   const addData=(event)=>{
    console.log(event.target.value);
   setTaskTitle(event.target.value);

   };
   const addTask=(event)=>{
    event.preventDefault();
    const task={
        title:taskTitle,
        status:status
    }
   setTaskList([...taskList, task])
   }

   const deleteData=(index)=>{
    const con=window.confirm("Are u sure?");
    if(con==true){
        taskList.splice(index,1);
        setTaskList([...taskList]);
    }

   }
    const changeStatus=(task)=>{
        let i=taskList.findIndex(work=>work==task);
        let status=taskList[i].status;
        console.log(status);
        if(status=="active"){
            taskList[i].status="deactive";
            setTaskList([...taskList]);
        }
        else{
            taskList[i].status="active";
            setTaskList([...taskList]);
        }
    }
    
return<>
<div className="container">
    <div className="row mt-6">
      <div className="col md-4 mt-5">
      <input className="form-control" onChange={addData} placeholder="Enter here"></input>
      </div>
      <div className="col md-4 mt-5">
      <select className="form-control" onChange={(e)=>setStatus(e.target.value)}>
        <option value="active">Select Status</option>
        <option value="active">Active</option>
        <option value="deactive">Deactive</option>
      </select>
      </div>
      <div className="col md-4 mt-5">
        <button onClick={addTask} className="btn" style={{borderRadius:"100%",backgroundColor:"#002147"}} id="btn-2" class="popup-button"><i class="fa fa-plus" style={{fontSize:"24px"}}></i></button>
      </div>
    </div>
   
    <div className="row mt-4">
        <table className="table table-hover table-responsive">
            <thead>
            <tr style={{backgroundColor:"#FF9999"}}>
                <th>S.No.</th>
                <th>Task</th>
                <th>Time</th>
                <th>Date</th>
                <th>Status</th>
                <th>Edit</th>
                <th>Remove</th>
            </tr>
            </thead>
            <tbody>
                {taskList.map((task,index)=>{
                    return <tr key={index}>
                    <td>{index+1}</td>
                    <td>{task.title}</td>
                    <td>{currentTime}</td>
                    <td>{currentDate}</td>
                    <td style={{cursor:'pointer'}} onClick={()=>changeStatus(task)}>{task.status=="active"?"Deactive":"active"}</td>
                    <td style={{cursor:'pointer'}}><i className="fas fa-edit" ></i></td>
                    <td style={{cursor:'pointer'}}><i className="far fa-trash-alt" onClick={()=>deleteData(index)}></i></td>
                </tr>
                })}
               

            </tbody>


        </table>

    </div>

</div>
</>
}
export default TodoList;