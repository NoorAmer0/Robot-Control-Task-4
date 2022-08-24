  function getDate() {
    return new Date().toISOString().slice(0, 10);
    }

  function getTime() {
    return new Date().toLocaleTimeString();
    }

  function storeBtnInfo(id){
      let motionInfo = {
      "date": getDate(),
      "time":getTime(),
      "direction":id }
      info = JSON.stringify(motionInfo)
      $.ajax({
         url:"/test",
         type:"POST",
         contentType: "application/json",
         data: JSON.stringify(info)});

        }

