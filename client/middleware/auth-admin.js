export default function({$auth,redirect}){
    let user=$auth.user;
    if(user &&user.is_staff){

    }
    else{
        redirect('/')
    }
}