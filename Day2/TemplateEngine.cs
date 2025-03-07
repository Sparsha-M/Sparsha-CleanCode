
namespace TemplateEngine;

public class TemplateEngine
{
    private string myName;
    private string myCompany;

    public string Evaluate()
    {
        return $"Hello {myName} {myCompany}";
    }
    
    public void SetName(string name)
    {
        myName = name;
    }

    public void SetCompany(string company)
    {
        myCompany = company;
    }   

}
