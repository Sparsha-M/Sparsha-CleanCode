using Microsoft.VisualStudio.TestPlatform.ObjectModel.DataCollection;


namespace TemplateEngine.Tests;

[TestFixture]
public class TemplateEngineTests
{
    [SetUp]
    public void Setup()
    {
    }

    [TestCase("Sree")]
    public void GivenOneVariable_Evaluate_TemplateEngine(string name)
    {
        //Arrange
        TemplateEngine templateEngine   = new TemplateEngine();
        templateEngine.SetName(name);

        //Act
        var result = templateEngine.Evaluate();


        //Assert
        Assert.That("Hello Sree", Is.EqualTo(result));
    }

    [TestCase("SPARSHA", "Siemens_Healthcare")]
    public void GivenTwoVariables_Evaluate_TemplateEngine(string name, string company)
    {
        //Arrange
        TemplateEngine templateEngine = new TemplateEngine();
        templateEngine.SetName(name);
        templateEngine.SetCompany(company);

        //Act
        var result = templateEngine.Evaluate();

        //Assert
        Assert.That("Hello SPARSHA Siemens_Healthcare", Is.EqualTo(result));
    }
}