import { Entity, Column, ManyToOne } from 'typeorm';
import { ChatEntity } from './chat.entity';

@Entity('message')
export class MessageEntity {

    @Column({ type: 'varchar', default: 'question' })
    type: string;

    @Column({ type: 'text', default: '', nullable: false })
    content: string;

    @ManyToOne(()=>ChatEntity, (chat)=>chat.messages, { nullable: false })
    chat: ChatEntity;

}