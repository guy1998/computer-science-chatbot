import { ChatEntity } from "src/chats/entities/chat.entity";
import { Column, Entity, OneToMany, PrimaryGeneratedColumn } from "typeorm";

@Entity('user')
export class UserEntity {

    @PrimaryGeneratedColumn('uuid')
    id: string

    @Column({ nullable: false })
    name: string

    @Column({ nullable: false })
    surname: string

    @Column({ nullable: false })
    email: string

    @Column({ nullable: false })
    password: string

    @OneToMany(()=>ChatEntity, chat=>chat.user)
    chats?: ChatEntity[]


}
