import { Entity, JoinColumn, ManyToOne, OneToMany, PrimaryGeneratedColumn } from "typeorm";
import { MessageEntity } from "./message.entity";
import { UserEntity } from "src/users/entities/user.entity";

@Entity("chat")
export class ChatEntity {

    @PrimaryGeneratedColumn('uuid')
    chatId: string;

    @OneToMany(()=>MessageEntity, (message)=>message.chat)
    messages?: MessageEntity[];

    @ManyToOne(()=>UserEntity, (user)=>user.chats, { nullable: false })
    user: UserEntity;

}
