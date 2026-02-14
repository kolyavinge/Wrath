class SendMessageResult:

    notSended = 0
    sended = 1


SendMessageResult.sendedAsBytes = SendMessageResult.sended.to_bytes(1)
