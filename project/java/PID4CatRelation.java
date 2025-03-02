package None;

import java.util.List;
import lombok.*;






/**
  A relation between pid4cat handles or between a pid4cat handle and other resources identified by a PID.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class Pid4CatRelation  {

  private String relationType;
  private RelatedIdentifier relatedIdentifier;
  private ZonedDateTime datetimeLog;

}
