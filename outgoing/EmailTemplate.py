from XMLforDMCA.parsedData.JsonConverter import (Title, IP_Address, Contact, Type, FileName, SubType_Protocol, Timestamp)


def generated_email_subject():
    subject = 'NOTICE: Copyright Infringement Warning'
    print(subject)
    return subject


def generated_email_body():
    body = f"""
    Dear {IP_Address},
    
    You are receiving this message to bring to your attention a matter of urgent importance regarding an infringement of copyright. It has come to our attention that you have unlawfully accessed content owned by {Contact} via {SubType_Protocol} at {Timestamp}.
    
    Details of Infringement:
    
    Description of Infringing Content: {Title} owned by {Contact} was unlawfully accessed.
    Location of Infringement: {Type}
    Original Work Details: {FileName}
    
    The copyright holder for the aforementioned content requests that you take immediate action to address this infringement.
    
    Specifically, we ask that you:
    
    1. Remove the Infringing Content: Please remove or disable access to the infringing material.
    2. Confirm Removal: Once the content has been removed, kindly confirm by replying to this email with a written acknowledgment.
    
    Please be aware that failure to address this issue promptly may result in further legal action to protect intellectual property rights.
    
    We also ask that you refrain from future use and sharing of the Rights Owners’ materials and property. In complying with this notice, you should not destroy any evidence that may be relevant in a lawsuit relating to the infringement alleged; including all associated electronic documents and data relating to the presence of the infringing items on your site, which shall be preserved while disabling public access, irrespective of any document retention or corporate policy to the contrary.
    
    Thank you for your prompt attention to this matter.
    
    Sincerely,
    
    [Name]
    [Your Position]
    [Your Company/Organization Name]
    [Your Contact Information]
    [Your Email Address]
    """

    print(body)
    return body
