import { response } from 'express';
import Conversation from '../models/conversation.model.js'
import Message from '../models/message.model.js'
export const sendMessage = async (req,res)=>{
    try {
        const {id: receiverId}=req.params;
        console.log(req.params.id)
        const {message} = req.body;
        console.log(req.body);
        const senderId= req.user._id;
        console.log(req.user._id)
        
        let conversation = await Conversation.findOne({
            participants:{$all:[senderId,receiverId]},
        })
        if(!conversation){
            conversation = await Conversation.create({
                participants:[senderId,receiverId],
            });
        }
        const newMessage = new Message({
            senderId,receiverId,message,
        })

        if(newMessage){
            conversation.messages.push(newMessage._id)
        }
        

        // await conversation.save();
        // await newMessage.save();

         //This will run in parallel

        await Promise.all([conversation.save(),newMessage.save()])
        res.status(201).json(newMessage);
        
    } catch (error) {
        console.log("Error in send message", error.message)
        res.status(500).json({error : "Internal Server Error"});
    }
};


export const getMessage = async (req,res)=>{
    try {
        const {id: receverId}=req.params;
        console.log(receverId)
        const senderId = req.user._id;
        console.log(senderId)

        const conversation = await Conversation.findOne({
            participants:{$all:[senderId,receverId]},
        }).populate("messages");


        res.status(200).json(conversation.messages);
        
    } catch (error) {
        console.log("Error in get message", error.message)
        res.status(500).json({error : "Internal Server Error"});
    }
}